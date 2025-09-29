"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : local_scope.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code showing execution time at the local scope.
 Usage      : python local_scope.py
===============================================================================
"""

# This file measures how long code takes to run when executed inside
# a function, providing a comparison point against global-level execution.

import time

ONE_BILLION = 1000000000

def loop() :
    result = 0
    for i in range (ONE_BILLION) :
        result += i
    return result

start_time = time . time ()
print ( " result : " , loop(), " Time : ", time.time() - start_time)