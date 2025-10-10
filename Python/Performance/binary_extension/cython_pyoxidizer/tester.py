"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : tester.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code showing the generation of Cython binary ext.
 Usage      : 1. Ensure the project is built as per README.md instructions
              2. python tester.py
===============================================================================
"""
import one_billion_loop as compiled_loop

compiled_loop.run_loop()