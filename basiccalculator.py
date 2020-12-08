#!/bin/python3


cycle = 0
choice = 0

def the_calculator():
    while True:
        global cycle
        if cycle == 0:
            firstnum = eval(input('''

type number, then press enter.

> '''))
        if cycle == 1:
            firstnum = total
        cycle = 1
        choice = input('''

type its number and press enter.

1. multiply
2. divide
3. subtract
4. add
5. CLEAR


> ''')
        if choice != '5':
            newnum = eval(input('''

type a second number

> '''))

###########   HOW TO COMPLICATE THE LIVING FUCK OUT OF SHIT

    #     INT or FLOAT

        floater = 1.0
        integer = 1

    #     FIRSTNUM int or float
   #     if type(eval(firstnum)) == type(floater):
   #         firstnu = float(firstnum)
   #     if type(eval(firstnum)) == type(integer):
   #         firstnum = int(firstnum)

    #     NEWNUM int or float
   #     if type(eval(newnum)) == type(floater):
   #         newnum = float(newnum)
   #     if type(eval(newnum)) == type(integer):
   #         newnum = int(newnum)

    #     IF one is a float
   #     if type(newnum) != type(firstnum):
   #         newnum = float(newnum)


        # calling functions add, div, sub, mult.
        am = 0
        while True:
            if am == 1:
                break
            if choice == '1':
                total = mult(firstnum, newnum)
            elif choice == '2':
                total = div(firstnum, newnum)
            elif choice == '3':
                total = sub(firstnum, newnum)
            elif choice == '4':
                total = add(firstnum, newnum)
            elif choice == '5':
                cycle = 0
                the_calculator()
            am += 1
        # Removing the decimal point from a float if it can be an integer.
        if type(total) == type(floater):
            check_list = [i for i in str(total)]
            if check_list[-2] == '.':
                num_list = [x for x in str(total)]
                if num_list[-2] == '.':
                    if num_list[-1] == '0':
                        for i in range(2):
                            num_list.pop(-1)
                        num_list = str(num_list).strip('[]')
                        num_list = str(num_list).strip(',')
                        total = int(total)
        if choice == '1':
            choice = ' X '
        if choice == '2':
            choice = ' / '
        if choice == '3':
            choice = ' - '
        if choice == '4':
            choice = ' + '

        print('')
        print(firstnum, choice, newnum)
        print('')
        print(total)


def add(a, b):
    sum = a + b
    return sum

def mult(a, b):
    sum = a * b
    return sum

def div(a, b):
    sum = a / b
    return sum

def sub(a, b):
    sum = a - b
    return sum

def cycling():
    global cycle
    if cycle == 1:
        newloc()

the_calculator()
