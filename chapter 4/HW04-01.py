'''
@author Sai
File name: HW04-01.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is reads the input from the user and calculates the factors using sympi
'''

from sympy import factor
from sympy import Symbol

if __name__ == '__main__':
    try:
        expr = input('enter the input you want to check the factorization for: ')
        x = Symbol('x')
        y = Symbol('y')
        #expr = x**2 - 5*x - 6
        factors = factor(expr)
        print(factors)
    except ValueError as ve:
        print(f"exception raised is {ve}")
            
            



        
        

