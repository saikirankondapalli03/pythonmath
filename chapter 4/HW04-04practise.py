from sympy import Poly, Symbol, solve_poly_inequality
x = Symbol('x')
ineq_obj = -x**2 + 4 < 0
lhs = ineq_obj.lhs
p = Poly(lhs, x)
rel = ineq_obj.rel_op
solve_poly_inequality(p, rel)



from sympy import Symbol, Poly, solve_rational_inequalities
x = Symbol('x')
ineq_obj = ((x-1)/(x+2)) > 0
lhs = ineq_obj.lhs
numer, denom = lhs.as_numer_denom()
p1 = Poly(numer)
p2 = Poly(denom)
rel = ineq_obj.rel_op
result= solve_rational_inequalities([[((p1, p2), rel)]])
print(result)


from sympy import Symbol, solve, solve_univariate_inequality, sin
x = Symbol('x')
ineq_obj = sin(x) - 0.6 > 0
result_1= solve_univariate_inequality(ineq_obj, x, relational=False)
print(result_1)


