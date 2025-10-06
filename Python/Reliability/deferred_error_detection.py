
"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : deferred_error_detection.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating undetected error in else-branch
 Usage      : python deferred_error_detection.py
===============================================================================
"""

# This file illustrates a NameError occurs in the else-branch, but because the
# branch is never executed, the program terminates without issue.

if True:
    print("This line is being executed")
else:
    ppppprint ( " This is a NameError " ) # Intentional issue to demonstrate lack of compile-time checking