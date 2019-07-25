'''
@author Sai
File name: HW06-01.py
Date created: 7/23/2019
Date last modified: 7/23/2019
Python Version: 3.1
This file outputs the square with side of radius and then fits circle inside the square

'''

from matplotlib import pyplot as plt

def draw_circle(x,y):
    circle = plt.Circle((x, y), radius = 0.5, ec='b',fc='99383')
    return circle

if __name__ == '__main__':
    ax = plt.axes(xlim = (0, 6), ylim = (0, 6))
    square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed = True)
    y = 1.5
    ax.add_patch(square)
    while y < 5:
        x = 1.5
        while x < 5:
            c = draw_circle(x, y)
            ax.add_patch(c)
            x += 1.0
        y += 1.0
    plt.show()
