'''
@author Sai
File name: HW07-04.py
Date created: 7/30/2019
Date last modified: 7/30/2019
Python Version: 3.1
This file finds the length of the arc as per the formula mentioned in the text book
'''


from sympy import Derivative, Integral, Symbol, sqrt, SympifyError, sympify

def find_length(fx, var, a, b):
    deriv = Derivative(fx, var).doit()
    #as per the formula mentioned in the text book
    length = Integral(sqrt(1+deriv**2), (var, a, b)).doit().evalf()
    return length

if __name__ == '__main__':
    input_function = input('Enter a function in one variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter the lower limit of the variable: '))
    b = float(input('Enter the upper limit of the variable: '))
    
    try:
        input_function = sympify(input_function)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        result = find_length(input_function, var, a, b)
        print(f'Length of {input_function} between {a} and {b} is: {result}')
