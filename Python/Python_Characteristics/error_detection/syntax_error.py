"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : syntax_error.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate SyntaxError in Python
 Usage      : python syntax_error.py
===============================================================================
"""

# Missing tokens, or tokens that do not conform to Python’s syntax
# rules are considered SyntaxError.

if True:
    print("This line is being executed")
else  # Colon intentionally omitted to demonstrate a SyntaxError.
    print("Missing ':' from the above else statement ")