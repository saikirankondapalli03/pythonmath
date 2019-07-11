'''
@author Sai
File name: HW01-05.py
Date created: 7/10/2019
Date last modified: 7/10/2019
Python Version: 3.1
This file is for giving exit power to the user for odd numbers
'''

import sys

initial_value= 0
offset= 9 

def print_odd():
    lst= []
    global initial_value
    global offset
    while initial_value < offset:
        lst.append(2*initial_value+1)
        initial_value += 1
    offset = initial_value + 9 
    print ( len(lst))
    yield lst


if __name__ == '__main__':
    try:
        while True:
            lst = print_odd()
            print(f'printing next 9 odd numbers {next(lst)}')
            answer = input('Do you want to exit? (y) for yes ')
            if answer == 'y':
                break   
    except ValueError as ve:
            print(f"Invalid number with {ve}")

