#!/bin/python3

list = []

def any(list):
    global element
    for i in list:
        if element:
            return True
        return False

while True:
    choice2 = input('''add item or remove item
 ''')

    if choice2.lower() == 'add':
        list.append(input('''type object you would like to add to list
 '''))
        print(list)

    elif choice2.lower() == 'remove':
        print(list)
        element = input(''' Which item would you like to remove?
 ''')
        element.lower()
        if True:
            print('found item')
            found_listitem = list.index(element)
            list.pop(int(found_listitem))
            print(list)
        else:
            print('sorry could not find that item, please try agian')
    else:
        print(' ERROR, "add" or "remove" are the only valid answers')
