"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : ast_demo.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate the Abstract Syntax Tree 
              (AST) process in Python
 Usage      : python ast_demo.py
===============================================================================
"""

import ast

code = """
def double(x):
    return x * 2
print(double(5))
"""
tree = ast.parse(code)

# Dumps the AST content of the 'double' method
print(ast.dump(tree, indent=4))