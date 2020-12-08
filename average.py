#!/bin/python3

# METHODS..                types of methods
#                      1, instance method
#                      2. class method
#                      3. static methods
import time

class average_2_nums:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def avg(self):
        return (self.m1 + self.m2)/2


class average_3_nums:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

def choice():
    while True:

        decide = input("""


       -- CHOOSE AN OPTION--

1.  Type 'two' to get average of two numbers

2.  Type 'three' for average of 3 numbers

3.  To quite type 'quite'

> """)

        if decide.lower() == 'two':
            choice = input('''

choose 2 numbers seperated by a single space : ''')
            choice1 = choice.split()
            s1 = average_2_nums(int(choice1[0]), int(choice1[1])).avg()

        elif decide.lower() == 'three':
            choice = input('''

choose 3 numbers seperated by a single space : ''')
            choice1 = choice.split()
            s1 = average_3_nums(int(choice1[0]), int(choice1[1]), int(choice1[2])).avg()

        elif decide.lower() == 'quite':
            exit()

        else:
            print('''

Error did not understand, please type again''')

        print(choice1)
        print(s1)
        time.sleep(4)

choice()

# fetching values using axises and to modify the variable use mutators
