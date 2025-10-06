/*
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : main.rs
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate bounded_latency in rust
 Usage      : This is a supplement to signal_handler_tester.py. First, build
              the binary by running cargo build. Then, move the binary to the 
              same location as signal_handler_tester.py and execute:
              python signal_handler_tester.py
===============================================================================
*/

use regex::Regex;
use std::time::{SystemTime, UNIX_EPOCH};
use std::io::{self, Write};
use std::process;


fn main() {
    let start_time = SystemTime::now().duration_since(UNIX_EPOCH).expect("error");
    ctrlc::set_handler(move || {

    let now = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .expect("error");

    let elapsed = (now - start_time).as_secs_f64();
        println!("Received SIGINT after {:.6} seconds", elapsed);
        process::exit(0);
    }).expect("Error setting Ctrl-C handler");

    let pattern = r"([a-zA-Z]+\s(4))";
    let text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, This is Word 4 vestibulum ut, placerat ac, adipiscing vitae, feli".repeat(100000000);

    let re = Regex::new(pattern).unwrap();
    
    
    println!("starting...");
    
    let _matches: Vec<_> = re.find_iter(&text).collect();
    
    let end_time = SystemTime::now().duration_since(UNIX_EPOCH).expect("error");
    let duration = end_time - start_time;
    
    println!("Finished: {:.2?} seconds", duration);
    io::stdout().flush().unwrap();
}