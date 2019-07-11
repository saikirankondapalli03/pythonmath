'''
@author Sai
File name: HW01-01.py
Date created: 4/16/2019
Date last modified: 4/16/2019
Python Version: 3.1
This file is for Enhanced Trajectile comparison
we need to calculate
a) the time of flight
b) maximum horizontal distance
c) maximum vertical distance traveled for each of the velocity and angle of projection combinations.
and finally 
Draw the trajectory of a body in projectile motion
'''
from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
   plt.plot(x, y)
   plt.xlabel('x-coordinate')
   plt.ylabel('y-coordinate')
   plt.title('Projectile motion of a ball')


def frange(start, final, interval):
   numbers = []
   while start < final:
      numbers.append(start)
      start = start + interval
   return numbers

def draw_trajectory(u, theta):
   theta = math.radians(theta)
   g = 9.8
   # Time of flight
   t_flight = 2*u*math.sin(theta)/g
   # Find time intervals
   intervals = frange(0, t_flight, 0.001)
   # List of x and y coordinates
   x = []
   y = []
   for t in intervals:
      x.append(u*math.cos(theta)*t)
      y.append(u*math.sin(theta)*t - 0.5*g*t*t)
   draw_graph(x, y)

if __name__ == '__main__':
   try:
      no_of_trajectories =  int(input('How many trajectories ?'))
      i =1 
      initial_velocity_list = []
      while i <= no_of_trajectories:
         initial_velocity = float(input(f'Enter the initial velocity for trajectory {i} (m/s):'))
         angle_projection = float(input(f'Enter the angle of projection for trajectory {i} (degrees):'))
         initial_velocity_list.append(initial_velocity)
         draw_trajectory(initial_velocity, angle_projection)
         i += 1
      plt.legend(initial_velocity_list)
      plt.show()
   except ValueError as ve:
      print(f'You entered an invalid input {ve}')



