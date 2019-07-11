'''
@author Sai
File name: HW01-02.py
Date created: 7/10/2019
Date last modified: 7/10/2019
Python Version: 3.1
This file is for multiplier with number and limit for number of multipliers
'''

import sys

def multi_table(number,multiple_limit):
     for i in range(1, multiple_limit+1):
        print('{0} x {1} = {2}'.format(number, i, number*i))

try:
    a = input('Enter a number: ')
    b = input('Enter the limit of multiples')
    if float(b).is_integer() and float(a).is_integer():
        multi_table(int(a),int(b))
except ValueError as ve:
    print(f"Invalid input with error {ve}")