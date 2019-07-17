'''
@author Sai
File name: HW04-01.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is for calculating the factors using sympi
'''

from sympy import factor,pprint
from sympy import Symbol

if __name__ == '__main__':
    #value = input('enter the input you want to check the factorization for: ')
    x = Symbol('x')
    y = Symbol('y')
    expr = x**2 + 2*x + 1
    print(factor(expr))
    pprint(factors)

            
            



        
        

