"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : signal_handle_tester.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating long running regex operation
 Usage      : First, compile main.rs using `cargo build`. Then,
              run the tester with `python signal_handle_tester.py
===============================================================================
"""
import subprocess
import time
import os
import signal

NUM_ITERATIONS = 5
WAIT_BEFORE_TERMINATE = 5  # seconds

response_times = []

for i in range(NUM_ITERATIONS):
    print(f"\nIteration {i + 1}")

    # Start the Rust receiver
    proc = subprocess.Popen(
        ["./signal_handling"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1
    )

    # Allow some time before sending SIGINT
    time.sleep(WAIT_BEFORE_TERMINATE)

    # Send SIGINT
    os.kill(proc.pid, signal.SIGINT)

    # Capture output
    stdout, stderr = proc.communicate()

    # Extract response time
    for line in stdout.splitlines():
        print(line)
        if "Received SIGINT" in line:
            response_time = float(line.strip().split()[-2])
            response_times.append(response_time)
            print(f"Captured: {line.strip()}")

print("\nAll response times:", response_times)
if response_times:
    print("Average response time:", sum(response_times) / len(response_times))
