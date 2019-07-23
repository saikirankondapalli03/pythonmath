from sympy import Symbol, pprint, init_printing
def print_series(n):
# Initialize printing system with reverse order
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)

from sympy import simplify

from sympy import Symbol, solve

if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    print_series(int(n))
    x= Symbol('x')
    y= Symbol('y')
    expr = x*x + x*y + x*y + y*y
    res = expr.subs({x:1, y:2})
    res1= expr.subs({x:1-y})
    expr_subs = expr.subs({x:1-y})
    result= simplify(expr_subs)
    x = Symbol('x')
    expr = x - 5 - 7
    result_1 =solve(expr)
    print(result_1)