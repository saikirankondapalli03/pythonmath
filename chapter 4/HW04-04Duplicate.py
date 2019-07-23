from sympy import Poly, Symbol, solve_poly_inequality

x = Symbol('x')
ineq_obj = -x**2 + 4 < 0
lhs = ineq_obj.lhs
p = Poly(lhs, x)
rel = ineq_obj.rel_op
ans_1 = solve_poly_inequality(p, rel)
print(ans_1)

from sympy import Symbol, Poly, solve_rational_inequalities
x = Symbol('x')
ineq_obj = ((x-1)/(x+2)) > 0
lhs = ineq_obj.lhs
numer, denom = lhs.as_numer_denom()
p1 = Poly(numer)
p2 = Poly(denom)
rel = ineq_obj.rel_op
ans_2 = solve_rational_inequalities([[((p1, p2), rel)]])
print(ans_2)

from sympy import Symbol, solve, solve_univariate_inequality, sin
x = Symbol('x')
ineq_obj = sin(x) - 0.6 > 0
ans_3 = solve_univariate_inequality(ineq_obj, x, relational=False)
print(ans_3)



x = Symbol('x')
expr = x**2 - 4 > 0
print(expr.is_polynomial())


expr = 2*sin(x) + 3
print(expr.is_polynomial())

expr = (2+x)/(3+x)
print(expr.is_rational_function())

expr = 2+sin(x) 
print(expr.is_rational_function())

from sympy import sympify
res_6= sympify('x+3>0')
print(res_6)
