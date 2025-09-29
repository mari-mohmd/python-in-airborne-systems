"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : no_jit.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating execution time without JIT
 Usage      : python no_jit.py
===============================================================================
"""

# This file measures the performance impact of running Python functions
# without Just-In-Time (JIT) compilation. It provides a comparison against
# JIT-enabled execution to highlight potential improvements in execution time.

import time

ONE_BILLION = 1000000000

start_time = time.time()

def compiled_function():
    x = 0
    for i in range(ONE_BILLION):
        x+=i
    return x

print("Finished x is:", compiled_function(), "; Duration:", time.time() - start_time, "seconds")