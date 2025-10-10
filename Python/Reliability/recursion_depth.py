"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : recursion_depth.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating recursion_depth limitation
 Usage      : python recursion_depth.py
===============================================================================
"""
import sys

# Recursion limit can be retrieved in Python. 
max_depth = sys.getrecursionlimit()
print("Current recursion limit:", max_depth)

# Recursive function
def do_recursion(n):
    for i in range(1,n+1):
    # will crash with RecursionError
        do_recursion(i)
    return


do_recursion(max_depth)

