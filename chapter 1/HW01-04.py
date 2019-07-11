'''
@author Sai
File name: HW01-04.py
Date created: 7/10/2019
Date last modified: 7/10/2019
Python Version: 3.1
This file is for enhanced unit converter
'''

import sys

from fractions import Fraction
def add(a, b):
    print('Result of Addition: {0}'.format(a+b))

def subtract(a,b):
    print('Result of subtract: {0}'.format(a-b))

def divide(a,b):
    print('Result of divide: {0}'.format(a//b))

def multiply(a,b):
    print('Result of multiply: {0}'.format(a*b))


if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a,b)
        if op == 'Subtract':
            subtract(a,b)
        if op=='Divide':
            divide(a,b)
        if op=='Multiply':
            multiply(a,b)
    except:
        print(f"Invalid input with error {sys.exc_info()[0]}")
