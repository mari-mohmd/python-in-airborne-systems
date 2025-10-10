"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : bounded_latency_multi_thread.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate bounded_latency and GIL impact
 Usage      : python bounded_latency_multi_thread.py
              for profiling: 1. mprof run python bounded_latency_multi_thread.py
                             2. mprof plot   
===============================================================================
"""

# This demo illustrates the impact of the Global Interpreter Lock (GIL) 
# on CPU-bound tasks when using multiple threads in Python. 

# Due to the GIL, only one thread executes Python bytecode at a time, 
# which limits the potential speedup from multi-threading. 
# This effect is especially visible in CPU-bound tasks, 
# where threads are forced to run sequentially rather than in parallel.
# In this example all sensors failed.
# Output: 
#   sens1 finished in 1.11s, expected <= 1s, delay 0.11s
#   sens2 finished in 1.12s, expected <= 1s, delay 0.12s
#   sens3 finished in 1.15s, expected <= 1s, delay 0.15s
#   sens4 finished in 1.16s, expected <= 1s, delay 0.16s


import threading
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


threads = []
start_time = time.time()

# Create and start all threads
for i in range(1, NUM_SENSORS + 1):
    t = threading.Thread(target=process, args=(f"sens{i}", start_time, EXPECTED_FINISH_TIME_SEC))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()