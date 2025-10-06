/*
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : one-billion-loop.rs
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate bounded_latency in rust
 Usage      : rustc -C opt-level=0 one-billion-loop.rs
===============================================================================
*/

use std::time::{Instant};

fn main () {
    let start_time = Instant::now();
    let mut x : u64 = 0;
    for i in 1..1000000000 {
        x += i ;
    }
    let end_time = Instant::now();
    let duration = end_time.duration_since(start_time).as_secs_f64();
    println!(
        "Duration: {}", duration
    );

}