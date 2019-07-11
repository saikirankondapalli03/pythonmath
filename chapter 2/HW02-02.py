'''
@author Sai
File name: HW01-01.py
Date created: 7/10/2019
Date last modified: 7/10/2019
Python Version: 3.1
This file is for Quadratic function calculator
''' 

from pylab import plot,show,title, xlabel, ylabel, legend , savefig

x_values = [-5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5]
y_values = []
for x in x_values:
   y = x**2 + 2*x + 1
   print('x={0} y={1}'.format(x, y))
   y_values.append(y)
   
plot(x_values,y_values)

title('Quadratic equation second degree')
xlabel('x')
ylabel('y')
savefig('quadratic.png')
show()