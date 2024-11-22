#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import re

pattern = r"\b[A-Za-z0-9._%+-]+@gmail\.com\b"

text = """
Monty Python:
John Cleese john.cleese@python.org
Eric Idle eric.idle@yahoo.com
Terry Gilliam terry.gilliam@gmail.com
Michael Palin
Terry Jones terry.jones@gmail.com
Graham Chapman
"""

email_gmail = re.findall(pattern, text)
print(email_gmail)  
