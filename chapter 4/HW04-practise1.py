from sympy import Symbol, expand
x=Symbol('x')
print(x+x+1)


from sympy import symbols,factor,pprint

x,y,z = symbols('x,y,z')
s = x*y + x*y
print(s)

p = x**2 + 2*x+1
print(expand(p))

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
print(pprint(factors))
print(expand(factors))

from sympy import init_printing
init_printing(order='rev-lex')
pprint(p)