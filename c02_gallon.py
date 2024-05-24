#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

# constants of the problem
GAL_USA_LITRES = 3.785       
GAL_IMP_USA = 1.2

# input - insert data
litres = float(input("Litres: "))

# computations - core part of the program 
gal_usa = litres / GAL_USA_LITRES
gal_imp = gal_usa * GAL_IMP_USA

# output - visualize results
print("American gallons", gal_usa)
print("Imperial gallons", gal_imp)
