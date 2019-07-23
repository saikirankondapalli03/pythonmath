from sympy import solve,Symbol
x = Symbol('x')
expr = x**2 + 5*x + 4
solve(expr, dict=True)

a= Symbol('a')
b= Symbol('b')
c= Symbol('c')
expr = a*x*x + b*x + c
solve(expr, x, dict=True)


from sympy import Symbol, solve, pprint
s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')
expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr,t, dict=True)
pprint(t_expr)


x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12
solve((expr1, expr2), dict=True)


from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
plot((2*x + 3), (x, -5, 5))

p = plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3', show=False)
p.save('line.png')


