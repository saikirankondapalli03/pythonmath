from sympy import sympify
from sympy.core.sympify import SympifyError


try:
    x = Symbol('x')
    y = Symbol('y')
    expr1 = 2*x + 3*y - 6
    expr2 = 3*x + 2*y - 12
    maps= solve((expr1, expr2), dict=True)
    print(maps)
except SympifyError as e:
    print(f'Invalid input {e}')

