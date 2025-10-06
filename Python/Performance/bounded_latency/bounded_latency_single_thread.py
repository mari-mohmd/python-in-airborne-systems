"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : bounded_latency_single_thread.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate bounded_latency and GIL impact
 Usage      : python bounded_latency_single_thread.py
===============================================================================
"""

# This demo illustrates how Python processes CPU-bound tasks on the main thread,
# highlighting the role of the GIL in limiting guarantees of bounded latency.

# In this example, the processing time of each sensor increases sequentially, 
# as each sensor waits for the previous one to finish. 
# The results show that sensors 1–3 completed successfully, 
# while sensor 4 failed because it had to wait for the first three sensors
# to finish before starting.
# Output:
#   sens1 finished in 0.29s, expected <= 1s, delay -0.71s
#   sens2 finished in 0.57s, expected <= 1s, delay -0.43s
#   sens3 finished in 0.85s, expected <= 1s, delay -0.15s
#   sens4 finished in 1.14s, expected <= 1s, delay 0.14s

import time


NUM_SENSORS = 4
EXPECTED_FINISH_TIME_SEC = 1

# Simulate sensor processing functionality
def process(sensor_id, start_time, expected_finish_time_sec):

    some_num = 0

    for i in range(10_000_000):
        some_num += i
    end_time = time.time()
    actual_time = end_time - start_time
    delay = actual_time - expected_finish_time_sec
    print(
        f"{sensor_id} finished in {actual_time:.2f}s, expected <= {expected_finish_time_sec}s, delay {delay:.2f}s"
    )


start_time = time.time() # All sensors start at the same time, but they execute sequentially on the main thread.
for i in range (1, NUM_SENSORS + 1):
    process(f"sens{i}", start_time, EXPECTED_FINISH_TIME_SEC)

