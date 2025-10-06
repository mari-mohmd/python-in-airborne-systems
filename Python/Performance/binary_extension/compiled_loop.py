"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : compiled_loop.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating the use of binary extension 
 Usage      : python compiled_loop.py
===============================================================================
"""

import time
import one_billion_loop # Importing the binary module created by maturin

start_time= time.time()
print ( " Finished x is : " , one_billion_loop.compiled_function() , 
       " ..... Duration : " , time.time() - start_time , " seconds " )