'''
@author Sai
File name: HW07-01.py
Date created: 7/30/2019
Date last modified: 7/30/2019
Python Version: 3.1
This file checks if a function is continuous at given point
'''

from sympy import Limit, Symbol, sympify, SympifyError

def check_if_continuous(input_function, var, x):
    #check lt x->a+ f(x). my examples are
    '''
    a) 1/(x-1) => it is not continuous at 1 , but it is continuous at all other points
    b) 2*x-5 is continuous at all points 
    To understand more about continuous refer 
    => https://www.mathsisfun.com/calculus/continuity.html
    => https://www.mathsisfun.com/calculus/differentiable.html
    '''
    limit1_result = Limit(input_function, var, x, dir='+').doit()
    limit2_result = Limit(input_function, var, x, dir='-').doit()
    f_val = input_function.subs({var:x})

    if limit1_result == limit2_result:
        print(f'{input_function} is continuous at {x}')
    else:
        print(f'{input_function} is not continuous at {x}')
    
if __name__ == '__main__':
    input_function = input('Enter a function in one variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter the point to check the continuity at: '))
    try:
        input_function = sympify(input_function)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        d = check_if_continuous(input_function, var, a)
