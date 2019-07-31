'''
@author Sai
File name: HW07-02.py
Date created: 7/30/2019
Date last modified: 7/30/2019
Python Version: 3.1
This file finds the gradient descent
Use gradient descent to find the minimum value of a
single variable function.
'''
from sympy import Derivative, Symbol, sympify, solve
import matplotlib.pyplot as plt

def grad_descent(x0, f1x, x): #(2,4*x,x)
    # check if f1x=0 has a solution
    result = solve(f1x)
    #if result is present 
    if not result:
        print(f'Cannot continue, solution for {f1x}=0 does not exist')
        return None
    epsilon =  1e-6 #0.0000001
    step_size = 1e-4 #0.00001
    x_old = x0
    x_new = x_old - step_size*f1x.subs({x:x_old}).evalf() # ideally it is f(x)= f(old)-stepsize*f1(x) at x=x_old

    # list to store the X values traversed
    x_traversed = []
    while abs(x_old - x_new) > epsilon:
        x_traversed.append(x_new)
        x_old = x_new
        x_new = x_old-step_size*f1x.subs({x:x_old}).evalf()

    return x_new, x_traversed #x_traversed is an array that have all x_new's that satisfies x_old-x_new > epsilon

def frange(start, final, interval):
    '''
    generate random numbers from -1 to 1 in steps of 0.001 ==> so total of 200 points for plotting the equation
    '''
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    
    return numbers

def create_plot(x_traversed, f, var):
    # plot the graph for the equation
    x_val = frange(-1, 1, 0.01)
    f_val = [f.subs({var:x}) for x in x_val]
    # for every value of x => find the value of y => so for 200 x points => 200 ypoints will be present
    #for the range of values from -1 to 1 
    plt.plot(x_val, f_val, 'o') # so this line plots 2*x**2 for values of x from -1 to 1 insteps of 0.001

    # calculate the function value at each of the intermediate
    # points traversed i.e where we iterated on differential side of equation 
    f_traversed = [f.subs({var:x}) for x in x_traversed]
    plt.plot(x_traversed, f_traversed, 'r.')
    plt.legend(['Function', 'Intermediate points'], loc='best')
    plt.show()

if __name__ == '__main__':

    f = input('Enter a function in one variable: ') # 2*x**2
    var = input('Enter the variable to differentiate with respect to: ') #x
    var0 = float(input('Enter the initial value of the variable: ')) #2
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit() #find derivative ==> 4x
        var_min, x_traversed = grad_descent(var0, d, var) # ==> (2,4*x,x)
        if var_min:
            print('{0}: {1}'.format(var.name, var_min))
            print('Minimum value: {0}'.format(f.subs({var:var_min})))
            create_plot(x_traversed, f, var)
