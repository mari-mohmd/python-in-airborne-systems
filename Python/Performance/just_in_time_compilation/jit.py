"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : jit.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating execution time with JIT enabled
 Usage      : python jit.py
===============================================================================
"""

# This file measures the performance impact of applying Just-In-Time (JIT)
# compilation to Python functions. It provides a comparison with standard
# (no_JIT) execution to highlight potential improvements in execution time.

import time
from numba import jit

ONE_BILLION = 1000000000

start_time = time.time()

@jit
def compiled_function():
    x = 0
    for i in range(ONE_BILLION):
        x+=i
    return x

print("Finished x is:", compiled_function(), "; Duration:", time.time() - start_time, "seconds")