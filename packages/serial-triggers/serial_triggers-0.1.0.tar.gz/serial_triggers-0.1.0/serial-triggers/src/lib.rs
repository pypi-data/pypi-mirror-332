use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;
use serialport::SerialPort;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::{mpsc, Arc, Mutex};
use std::thread;
use std::time::{Duration, Instant};

#[derive(Clone, Copy, PartialEq)]
enum QueueBehavior {
    Add,
    Discard,
    Block,
}

struct SerialEvent {
    value: i32,
    delay: Option<Duration>,
}

struct SerialWriterInner {
    port: Box<dyn SerialPort>,
    queue_behavior: QueueBehavior,
}

#[pyclass]
struct SerialWriter {
    inner: Arc<Mutex<SerialWriterInner>>,
    sender: mpsc::Sender<SerialEvent>,
    running: Arc<AtomicBool>,
}

#[pymethods]
impl SerialWriter {
    #[new]
    fn new(port_name: &str, baud_rate: u32, queue_behavior: &str) -> PyResult<Self> {
        let behavior = match queue_behavior {
            "add" => QueueBehavior::Add,
            "discard" => QueueBehavior::Discard,
            "block" => QueueBehavior::Block,
            _ => {
                return Err(PyValueError::new_err(
                    "Queue behavior must be 'add', 'discard', or 'block'",
                ))
            }
        };

        let port = serialport::new(port_name, baud_rate)
            .timeout(Duration::from_millis(1000))
            .open()
            .map_err(|e| PyRuntimeError::new_err(format!("Failed to open serial port: {}", e)))?;

        let inner = Arc::new(Mutex::new(SerialWriterInner {
            port,
            queue_behavior: behavior,
        }));

        // Create channel for thread communication
        let (sender, receiver) = mpsc::channel();

        let running = Arc::new(AtomicBool::new(true));
        let inner_clone = inner.clone();
        let running_clone = running.clone();

        thread::spawn(move || {
            process_queue(inner_clone, receiver, running_clone);
        });

        Ok(SerialWriter { inner, sender, running })
    }

    fn write(&self, value: i32) -> PyResult<()> {
        let event = SerialEvent { value, delay: None };

        self.add_to_queue(event)
    }

    fn write_delayed(&self, value: i32, delay_ms: u64) -> PyResult<()> {
        let event = SerialEvent {
            value,
            delay: Some(Duration::from_millis(delay_ms)),
        };

        self.add_to_queue(event)
    }

    fn set_queue_behavior(&self, behavior: &str) -> PyResult<()> {
        let new_behavior = match behavior {
            "add" => QueueBehavior::Add,
            "discard" => QueueBehavior::Discard,
            "block" => QueueBehavior::Block,
            _ => {
                return Err(PyValueError::new_err(
                    "Queue behavior must be 'add', 'discard', or 'block'",
                ))
            }
        };

        let mut inner = self.inner.lock().unwrap();
        inner.queue_behavior = new_behavior;
        Ok(())
    }

    fn get_queue_behavior(&self) -> PyResult<String> {
        let inner = self.inner.lock().unwrap();
        let behavior = match inner.queue_behavior {
            QueueBehavior::Add => "add",
            QueueBehavior::Discard => "discard",
            QueueBehavior::Block => "block",
        };
        Ok(behavior.to_string())
    }

    fn close(&mut self) -> PyResult<()> {
        self.running.store(false, Ordering::SeqCst);
        Ok(())
    }

    #[staticmethod]
    fn list_ports() -> PyResult<Vec<String>> {
        let ports = serialport::available_ports()
            .map_err(|e| PyRuntimeError::new_err(format!("Failed to list serial ports: {}", e)))?;

        let port_names = ports.into_iter().map(|info| info.port_name).collect();

        Ok(port_names)
    }
}

impl SerialWriter {
    fn add_to_queue(&self, event: SerialEvent) -> PyResult<()> {
        let inner = self.inner.lock().unwrap();

        match inner.queue_behavior {
            QueueBehavior::Add => {
                // Always add to queue
                self.sender
                    .send(event)
                    .map_err(|_| PyRuntimeError::new_err("Failed to send event to queue"))?;
                Ok(())
            }
            QueueBehavior::Discard => {
                // Only add if queue is empty, otherwise discard
                // Note: mpsc doesn't have a direct way to check if the queue is empty
                // We'll use try_send which doesn't exist, so we'll always send
                // and implement the discard logic in the receiver
                self.sender
                    .send(event)
                    .map_err(|_| PyRuntimeError::new_err("Failed to send event to queue"))?;
                Ok(())
            }
            QueueBehavior::Block => {
                // Will block if queue is full (which doesn't happen with mpsc)
                // For block behavior, we'll implement it in the receiver
                self.sender
                    .send(event)
                    .map_err(|_| PyRuntimeError::new_err("Failed to send event to queue"))?;
                Ok(())
            }
        }
    }
}

fn process_queue(
    inner: Arc<Mutex<SerialWriterInner>>,
    receiver: mpsc::Receiver<SerialEvent>,
    running: Arc<AtomicBool>,
) {
    // For discard and block behaviors, we need to track if we're currently processing an event
    let mut is_processing = false;

    while running.load(Ordering::SeqCst) {
        // Check if we should process the next event based on queue behavior
        let should_process = {
            let inner_guard = inner.lock().unwrap();
            match inner_guard.queue_behavior {
                QueueBehavior::Add => true,
                QueueBehavior::Discard => !is_processing,
                QueueBehavior::Block => !is_processing,
            }
        };

        if should_process {
            // Try to receive an event with timeout to allow checking the running flag periodically
            match receiver.recv_timeout(Duration::from_millis(100)) {
                Ok(event) => {
                    is_processing = true;

                    let mut inner_guard = inner.lock().unwrap();

                    // Convert the integer to bytes (assuming little-endian)
                    let bytes = event.value.to_le_bytes();

                    // Write the bytes to the serial port
                    if let Err(e) = inner_guard.port.write(&bytes) {
                        eprintln!("Failed to write to serial port: {}", e);
                    }

                    // If there's a delay specified, wait for the exact amount of time
                    if let Some(delay) = event.delay {
                        // Release the lock during the delay
                        drop(inner_guard);

                        let start = Instant::now();
                        while start.elapsed() < delay {
                            // Spin wait for precise timing
                            std::hint::spin_loop();

                            // Check if we should still be running
                            if !running.load(Ordering::SeqCst) {
                                return;
                            }
                        }

                        // Re-acquire the lock to write the next value
                        let mut inner_guard = inner.lock().unwrap();

                        // Write the same value again after the delay
                        if let Err(e) = inner_guard.port.write(&bytes) {
                            eprintln!("Failed to write delayed value to serial port: {}", e);
                        }
                    }

                    is_processing = false;
                }
                Err(mpsc::RecvTimeoutError::Timeout) => {
                    // Timeout occurred, just continue to check running flag
                    continue;
                }
                Err(mpsc::RecvTimeoutError::Disconnected) => {
                    // Sender has been dropped, exit the loop
                    break;
                }
            }
        } else {
            // We're not processing events right now, so just drain the queue
            while let Ok(_) = receiver.try_recv() {
                // Discard events
            }

            // Sleep a bit to avoid busy waiting
            thread::sleep(Duration::from_millis(10));
        }
    }
}

#[pymodule]
fn serial_triggers(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<SerialWriter>()?;
    Ok(())
}
