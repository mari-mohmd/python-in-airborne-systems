"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : bounded_latency_multi_process.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating bounded latency using multiprocessing.
 Usage      : python bounded_latency_multi_process.py
===============================================================================
"""

# This file simulates sensor processing tasks running in parallel processes.
# By using multiprocessing, the Global Interpreter Lock (GIL) is bypassed,
# allowing true concurrent execution on multiple CPU cores. This provides
# a comparison against single-threaded and multi-threaded versions for
# analyzing Python’s ability to meet bounded latency requirements.
# Output:
#   sens4 finished in 0.36s, expected <= 1s, delay -0.64s
#   sens2 finished in 0.36s, expected <= 1s, delay -0.64s
#   sens1 finished in 0.36s, expected <= 1s, delay -0.64s
#   sens3 finished in 0.37s, expected <= 1s, delay -0.63s

import time
import multiprocessing as mp

NUM_SENSORS = 4

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

if __name__ == "__main__":
    processes = []
    start_time = time.time()

    # Create and start all processes
    for i in range(1, NUM_SENSORS + 1):
        p = mp.Process(target=process, args=(f"sens{i}", start_time, 1))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()
