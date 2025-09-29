"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : indentation_error.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate IndentationError in Python
 Usage      : python indentation_error.py
===============================================================================
"""

# In Python, indentation defines the scope of code blocks, not
# used just for readability purposes. Indentation issues are
# detected before runtime

if True :
    print ( " Hello " )
else :
print ( " Indentation error " )