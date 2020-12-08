#!/bin/python3

# figuring out how scrapers work, as well as regular expressions library.
# reusable can be configured and adding into projects 

from bs4 import BeautifulSoup
import requests
import re

# insert any webpage in to pull phone number from page
web_page = requests.get("https://stackoverflow.com/legal/contact")
HTML = BeautifulSoup(web_page.content, features="lxml")
HTML_filtered = str(HTML)

age = []
zip = []
phone_numbers = []
blank = ''

lots_of_numbers = ' 713 939 3443 glehfdalkdf 94b 832 4839 alkdf 44b5554433 22x 45b 99xx'


age = re.findall(r'(?<!\d)\d{1,2}(?!\d)', blank)
zip = re.findall(r'\d{5}', blank)
phone_numbers = re.findall(r'[(]?\d{3}[)]?.?\d{3}.?\d{4}', HTML_filtered)
for i in phone_numbers:
    if re.findall(r'[a-z]', i):
        loc = phone_numbers.index(i)
        loc = int(loc)
        phone_numbers.pop(loc)

print(phone_numbers)
print(age)
print(zip)

# cant complete table with PANDAS because pandas library doesnt
# work for install yet
