/*
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : bounded_latency_multi_thread.rs
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate bounded_latency in rust
 Usage      : rustc -C opt-level=0 bounded_latency_multi_thread.rs
===============================================================================
*/

// This example runs multiple simulated sensor processing tasks in parallel 
// using Rust threads. Unlike Python, Rust has no Global Interpreter Lock (GIL),
// so CPU-bound tasks can execute concurrently across cores. The results can be
// compared with the single-threaded and Python versions to highlight differences
// in latency.
// Output:
//   sens4 finished in 0.05s, expected <= 0.10s, delay -0.05s
//   sens2 finished in 0.06s, expected <= 0.10s, delay -0.04s
//   sens1 finished in 0.06s, expected <= 0.10s, delay -0.04s
//   sens3 finished in 0.06s, expected <= 0.10s, delay -0.04s

use std::thread;
use std::time::{Instant};

const NUM_SENSORS: usize = 4;
const EXPECTED_FINISH_TIME_SEC: f64 = 0.1;

// Simulate sensor processing functionality
fn process(sensor_id: String, start_time: Instant, expected_finish_time_sec: f64) {
    let mut some_num: u64 = 0;

    for i in 0..10_000_000 {
        some_num = some_num.wrapping_add(i);
    }

    let end_time = Instant::now();
    let actual_time = end_time.duration_since(start_time).as_secs_f64();
    let delay = actual_time - expected_finish_time_sec;
    println!(
        "{} finished in {:.2}s, expected <= {:.2}s, delay {:.2}s",
        sensor_id, actual_time, expected_finish_time_sec, delay
    );
}

fn main() {
    let start_time = Instant::now();
    let mut handles = vec![];

    // Create and start all threads
    for i in 1..=NUM_SENSORS {
        let sensor_id = format!("sens{}", i);
        let start_time_clone = start_time.clone();

        let handle = thread::spawn(move || {
            process(sensor_id, start_time_clone, EXPECTED_FINISH_TIME_SEC);
        });

        handles.push(handle);
    }

    // Wait for all threads to finish
    for handle in handles {
        handle.join().unwrap();
    }
}
