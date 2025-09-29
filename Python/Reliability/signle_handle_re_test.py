"""
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : signle_handle_re_test.py
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code demonstrating long running regex operation
 Usage      : signle_handle_re_test.py
===============================================================================
"""
# This file simulates a long-running regex operation to test KeyboardInterrupt
# handling on single-threaded execution using binary extension libraries like `re`.


import re
import time

pattern = r'([a-zA-Z]+\s(4))'
text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, feli' * 10000000
start_time = time.time()
print ("starting...")
match = re.findall(pattern, text)
end_time = time.time()

print(f"Finished: {end_time - start_time} seconds")