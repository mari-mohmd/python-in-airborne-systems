"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : tokenization_demo.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate the tokenization 
              process in Python
 Usage      : python -m tokenize tokenization_demo.py
===============================================================================
"""

# When this code is executed with the '-m tokenize' flags, 
# it will output the tokenized content of the script.

def double(x):
    return x * 2

print(double(5))
