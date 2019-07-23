'''
@author Sai
File name: HW04-01.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is reads two expressions from the user and calculates the co-ordinates that satisfies both the equations
'''

from sympy import factor
from sympy import Symbol, SympifyError

'''
Plot the graph of an input expression
'''
from sympy import Symbol, sympify, solve
from sympy.plotting import plot

def plot_expression(expr1,expr2):
    y = Symbol('y')
    solutions1 = solve(expr1, y)
    solutions2 = solve(expr2, y)
    result = solve((expr1,expr2),dict=True)
    print(f"values are {result} " );
    expr_y_1 = solutions1[0]
    expr_y_2 = solutions2[0]
    plot(expr_y_1,expr_y_2)
    

if __name__=='__main__':
    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError as ve:
        print(f'Invalid input: {ve}')
    else:
        plot_expression(expr1,expr2)
        
            
            



        
        

