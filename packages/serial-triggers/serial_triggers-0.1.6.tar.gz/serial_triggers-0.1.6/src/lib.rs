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

enum ThreadCommand {
    WriteValue(u8),
    WriteDelayed(u8, Duration),
    SetQueueBehavior(QueueBehavior),
    Shutdown,
}

#[pyclass]
struct SerialWriter {
    sender: mpsc::Sender<ThreadCommand>,
    queue_behavior: Mutex<QueueBehavior>,
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

        // Create channel for thread communication
        let (sender, receiver) = mpsc::channel();

        // Open the serial port in the main thread
        let port = serialport::new(port_name, baud_rate)
            .timeout(Duration::from_millis(1000))
            .open()
            .map_err(|e| PyRuntimeError::new_err(format!("Failed to open serial port: {}", e)))?;

        // Spawn the worker thread with ownership of the port
        thread::spawn(move || {
            process_commands(port, receiver, behavior);
        });

        Ok(SerialWriter {
            sender,
            queue_behavior: Mutex::new(behavior),
        })
    }

    fn write(&self, value: u8) -> PyResult<()> {
        let behavior = *self.queue_behavior.lock().unwrap();

        match behavior {
            QueueBehavior::Add => {
                // Always add to queue
                self.sender
                    .send(ThreadCommand::WriteValue(value))
                    .map_err(|_| PyRuntimeError::new_err("Failed to send command to worker thread"))?;
            }
            QueueBehavior::Discard => {
                // Try to send, but don't worry if it fails due to a full queue
                let _ = self.sender.send(ThreadCommand::WriteValue(value));
            }
            QueueBehavior::Block => {
                // Will block if the receiver is not ready
                self.sender
                    .send(ThreadCommand::WriteValue(value))
                    .map_err(|_| PyRuntimeError::new_err("Failed to send command to worker thread"))?;
            }
        }

        Ok(())
    }

    fn write_delayed(&self, value: u8, delay_ms: u64) -> PyResult<()> {
        let delay = Duration::from_millis(delay_ms);
        let behavior = *self.queue_behavior.lock().unwrap();

        match behavior {
            QueueBehavior::Add => {
                // Always add to queue
                self.sender
                    .send(ThreadCommand::WriteDelayed(value, delay))
                    .map_err(|_| PyRuntimeError::new_err("Failed to send command to worker thread"))?;
            }
            QueueBehavior::Discard => {
                // Try to send, but don't worry if it fails due to a full queue
                let _ = self.sender.send(ThreadCommand::WriteDelayed(value, delay));
            }
            QueueBehavior::Block => {
                // Will block if the receiver is not ready
                self.sender
                    .send(ThreadCommand::WriteDelayed(value, delay))
                    .map_err(|_| PyRuntimeError::new_err("Failed to send command to worker thread"))?;
            }
        }

        Ok(())
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

        // Update the local copy of the behavior
        *self.queue_behavior.lock().unwrap() = new_behavior;

        // Send the new behavior to the worker thread
        self.sender
            .send(ThreadCommand::SetQueueBehavior(new_behavior))
            .map_err(|_| PyRuntimeError::new_err("Failed to send command to worker thread"))?;

        Ok(())
    }

    fn get_queue_behavior(&self) -> PyResult<String> {
        let behavior = *self.queue_behavior.lock().unwrap();
        let behavior_str = match behavior {
            QueueBehavior::Add => "add",
            QueueBehavior::Discard => "discard",
            QueueBehavior::Block => "block",
        };
        Ok(behavior_str.to_string())
    }

    fn close(&mut self) -> PyResult<()> {
        // Send shutdown command to the worker thread
        let _ = self.sender.send(ThreadCommand::Shutdown);
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

fn process_commands(
    mut port: Box<dyn SerialPort>,
    receiver: mpsc::Receiver<ThreadCommand>,
    mut queue_behavior: QueueBehavior,
) {
    // For discard behavior, we need to track if we're currently processing a command
    let mut is_processing = false;

    loop {
        // Determine if we should process the next command based on queue behavior
        let should_process = match queue_behavior {
            QueueBehavior::Add => true,
            QueueBehavior::Discard | QueueBehavior::Block => !is_processing,
        };

        if should_process {
            // Try to receive a command with timeout
            match receiver.recv_timeout(Duration::from_millis(100)) {
                Ok(command) => {
                    match command {
                        ThreadCommand::WriteValue(value) => {
                            is_processing = true;

                            // Convert the integer to bytes (assuming little-endian)
                            let bytes = value.to_le_bytes();

                            // Write the bytes to the serial port
                            if let Err(e) = port.write(&bytes) {
                                eprintln!("Failed to write to serial port: {}", e);
                            }

                            port.flush().unwrap();

                            println!("Wrote value: {}", value);

                            is_processing = false;
                        }
                        ThreadCommand::WriteDelayed(value, delay) => {
                            is_processing = true;

                            // Convert the integer to bytes (assuming little-endian)
                            let bytes = value.to_le_bytes();

                            // Write the bytes to the serial port
                            if let Err(e) = port.write(&bytes) {
                                eprintln!("Failed to write to serial port: {}", e);
                            }

                            port.flush().unwrap();

                            // Wait for the exact amount of time
                            let start = Instant::now();
                            while start.elapsed() < delay {
                                // Spin wait for precise timing
                                std::hint::spin_loop();
                            }

                            // Write the same value again after the delay
                            if let Err(e) = port.write(&bytes) {
                                eprintln!("Failed to write delayed value to serial port: {}", e);
                            }

                            port.flush().unwrap();

                            is_processing = false;
                        }
                        ThreadCommand::SetQueueBehavior(new_behavior) => {
                            queue_behavior = new_behavior;
                        }
                        ThreadCommand::Shutdown => {
                            // Exit the loop and terminate the thread
                            break;
                        }
                    }
                }
                Err(mpsc::RecvTimeoutError::Timeout) => {
                    // Timeout occurred, just continue
                    continue;
                }
                Err(mpsc::RecvTimeoutError::Disconnected) => {
                    // Sender has been dropped, exit the loop
                    break;
                }
            }
        } else {
            // We're not processing commands right now, so just drain the queue for discard behavior
            if queue_behavior == QueueBehavior::Discard {
                while let Ok(_) = receiver.try_recv() {
                    // Discard commands
                }
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
