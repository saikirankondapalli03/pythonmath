'''
@author Sai
File name: HW01-01.py
Date created: 7/10/2019
Date last modified: 7/10/2019
Python Version: 3.1
This file is for even-odd vending machine
'''

import sys

def print_odd():
    for i in range(1, 9):
        print(2*i+1)

def print_even():
    for i in range(1, 9):
        print(2*i)

try:
    input_val = input("Please enter the input:")
    
    if input_val=='1':
        print_odd()
    elif input_val=='2':
        print_even()
    else:
        print("please enter the valid input")
        sys.exit()      
except ValueError as ve:
        print(f"Invalid number with {ve}")