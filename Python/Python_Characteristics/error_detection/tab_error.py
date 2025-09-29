"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : tab_error.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate SyntaxError in Python
 Usage      : python tab_error.py
===============================================================================
"""

# In Python, spaces and tabs function differently for indentation. You
# can choose to use either spaces or tabs consistently for indentation
# within a block of code. Mixing spaces and tabs within the same block
# of code will lead to a TabError

if True :
    print ( " Run time execution " )
else:
    # This example uses different types of indentation (spaces and tabs).
    # which will cause a TabError.
	print ( " This line is indented with a tab " )
    print ( " This line is indented with 4 spaces " ) 