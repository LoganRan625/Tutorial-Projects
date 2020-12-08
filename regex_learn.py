#!/bin/python3
# finding phone numbers with regex

import re

#re stands for regular expression

text_one = 'abcdefghijklmnopqrstuvwxyz1234567890'
text_two = 'hello jim how is Dr. Mathews?, his phone number is 714-362-2233'

text_email = '''
megastupid@gmail.com
345stupidsilly@aol.com
328.234.9900
212.495.2209
564-234.4566
333 545 9345

'''

phone_numbers = []
phone_numbers = re.findall(r'\d{3}.\d{3}.\d{4}', text_email)
print(phone_numbers)
