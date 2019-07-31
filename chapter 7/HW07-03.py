'''
@author Sai
File name: HW07-03.py
Date created: 7/30/2019
Date last modified: 7/30/2019
Python Version: 3.1
This file finds the area enclosed by a straight line and a parabola
'''

from sympy import Integral, Symbol, SympifyError, sympify

def find_area(f1x, f2x, var, a, b):
    a = Integral(f1x-f2x, (var, a, b)).doit() #basic integral forumla with the help of sympy libraries
    return a

if __name__ == '__main__':
    f1x = input('Enter the upper function in one variable: ')
    f2x = input('Enter the lower upper function in one variable: ')
    var = input('Enter the variable: ')
    l = float(input('Enter the lower bound of the enclosed region: '))
    u = float(input('Enter the upper bound of the enclosed region: '))
    
    try:
        f1x = sympify(f1x)
        f2x = sympify(f2x)
    except SympifyError:
        print('One of the functions entered is invalid')
    else:
        var = Symbol(var)
        result = find_area(f1x, f2x, var, l, u)
        print(f'Area enclosed by {f1x} and {f2x} is: {result}')
