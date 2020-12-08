#!/bin/python3
# creates empty shell to build on 

import Basic

while True:
    text = input('basic > ')
    result, error = Basic.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)
