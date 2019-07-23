'''
@author Sai
File name: HW04-03.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is reads two expressions from the user and calculates the co-ordinates that satisfies both the equations
'''



from sympy import Symbol, pprint, init_printing
def print_series(n, x_value):
# Initialize printing system with reverse order
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)
    series_value = series.subs({x:x_value})
    print('Value of the series at {0}: {1}'.format(x_value, series_value))

from sympy import Symbol, summation, pprint

def print_series1(nth_term):
    a = Symbol('a')
    n = Symbol('n')
    d = Symbol('d')
    s = summation( a+(n-1)*d , (n, 1, nth_term))
    pprint(s)

if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    #x_value = input('Enter the value of x at which you want to evaluate the series: ')
    print_series1(n)
    #print_series(int(n), float(x_value))
