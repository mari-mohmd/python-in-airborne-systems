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
              run the tester: python signal_handle_tester.py <<signal test file>>
===============================================================================
"""
import subprocess
import time
import os
import signal
import sys

NUM_ITERATIONS = 5
WAIT_BEFORE_TERMINATE = 5  # seconds

response_times = []

for i in range(NUM_ITERATIONS):
    print(f"\nIteration {i + 1}")

    # Start the receiver
    proc = subprocess.Popen(["python", sys.argv[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Allow some time before sending SIGINT
    time.sleep(WAIT_BEFORE_TERMINATE)

    start_signal_time = time.time()
    # Send SIGINT
    os.kill(proc.pid, signal.SIGINT)

    stdout, stderr = proc.communicate()

    # Extract response time
    for line in stdout.splitlines():
        if "SIGINT" in line:
            response_time = float(line.split()[-2])  # extract the seconds
            response_times.append(response_time)
            print(line)

print("\nAll response times:", response_times)
print("Average response time:", sum(response_times) / len(response_times))
