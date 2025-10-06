
"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : tester.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: A generic tester. Runs a Python program 5 times,
              reports execution durations and WCET.
 Usage      : python tester.py <<python_program.py>>
===============================================================================
"""

import subprocess
import time
import sys

# Number of times to run the script
NUM_ITERATIONS = 5
wcet = 0
print(sys.argv[1])
for i in range(NUM_ITERATIONS):
    print(f"Starting iteration {i+1}...")
    start = time.perf_counter()
    # Run Python program and wait for it to finish
    proc = subprocess.Popen(["python", sys.argv[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if stderr:
        print(stderr)
        sys.exit(1)
    duration = time.perf_counter() - start
    print(f"Duration: {duration}")
    wcet = max(wcet, duration)

print(f"Estimated WCET: {wcet:.6f} seconds")
 

