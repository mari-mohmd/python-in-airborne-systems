"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : global_scope.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code showing execution time at the global level.
 Usage      : python global_scope.py
===============================================================================
"""

# This file measures how long code takes to run when executed directly
# at the module scope, without being wrapped in functions or threads.
# Useful for comparing execution behavior across different contexts.

import time

ONE_BILLION = 1000000000
start_time = time.time ()
result = 0
for i in range (ONE_BILLION):
    result += i
print ( " Time : ", time.time() - start_time )
