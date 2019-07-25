'''
@author Sai
File name: HW06-03.py
Date created: 7/23/2019
Date last modified: 7/23/2019
Python Version: 3.1
This file displays Hénon function with n as input
'''

import random
import matplotlib.pyplot as plt
from matplotlib import animation
def transform(p):
    x = p[0]
    y = p[1]
    x1 = y + 1 - 1.4*(x**2) 
    y1 = 0.3*x
    return x1, y1


def draw_Henon(n):
    # We start with (0, 0)
    x = [1]
    y = [1]
    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

def update_points(i, x, y, plot):
    plot.set_data(x[:i], y[:i])
    return plot


if __name__ == '__main__':
    n = int(input('Enter the number of points in Hénon function : '))
    x, y = draw_Henon(n)
    # Plot the points
    fig = plt.gcf()
    ax = plt.axes(xlim = (min(x), max(x)),
                  ylim = (min(y), max(y)))
    plot, = ax.plot([], [], 'o')
    anim = animation.FuncAnimation(fig, update_points,
                                   fargs=(x, y, plot),
                                   frames = len(x),
                                   interval = 5000,
                                   blit = True)
    plt.title('Henon function')
    plt.plot(x, y, 'o')
    plt.title('Hénon function with {0} points'.format(n))
    plt.show()

