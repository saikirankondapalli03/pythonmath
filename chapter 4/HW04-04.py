'''
@author Sai
File name: HW04-04.py
Date created: 7/21/2019
Date last modified: 7/21/2019
Python Version: 3.1
This file reads inequalities and outputs the boundary of a function
'''

from sympy import Poly, Symbol, solve_poly_inequality


def solve_poly_inequality_1(expression):
    print(f"function 1 ")
    x = Symbol('x')
    ineq_obj = expression #-x**2 + 4 < 0
    lhs = ineq_obj.lhs
    p = Poly(lhs, x)
    rel = ineq_obj.rel_op
    ans_1 = solve_poly_inequality(p, rel)
    print(f"ans_1 {ans_1}")
    return ans_1


from sympy import Symbol, Poly, solve_rational_inequalities

def solve_rational_inequalities_1(expression):
    print(f"function 2 ")
    x = Symbol('x')
    ineq_obj = expression #((x-1)/(x+2)) > 0
    lhs = ineq_obj.lhs
    numer, denom = lhs.as_numer_denom()
    p1 = Poly(numer)
    p2 = Poly(denom)
    rel = ineq_obj.rel_op
    ans_2 = solve_rational_inequalities([[((p1, p2), rel)]])
    #print(f"ans_2:{ans_2}")
    return ans_2

from sympy import Symbol, solve, solve_univariate_inequality, sin

def solve_univariate_inequality_1(expression):
    print(f"function 3 ")
    x = Symbol('x')
    ineq_obj = expression #sin(x) - 0.6 > 0
    ans_3 = solve_univariate_inequality(ineq_obj, x, relational=False)
    #print(f"ans_3:{ans_3}")
    return ans_3


from sympy import Symbol, SympifyError,sympify

if __name__=='__main__':
    expr1 = input('Enter your first expression in terms of x and y: ')
    try:
        expr1 = sympify(expr1)
        if expr1.lhs.is_polynomial():
            final_result = solve_poly_inequality_1(expr1)
        elif expr1.lhs.is_rational_function():
            final_result = solve_rational_inequalities_1(expr1)
        else:
            final_result = solve_univariate_inequality_1(expr1)
    except SympifyError as ve:
        print(f'Invalid input: {ve}')
    print(f"result is {final_result}")