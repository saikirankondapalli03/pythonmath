'''
@author Sai
File name: HW02-01.py
Date created: 7/10/2019
Date last modified: 7/10/2019
Python Version: 3.1
This file is for plotting x-axis (time) and y-axis(temperatures) in graph comparing two different cities
''' 
from pylab import plot,show,title, xlabel, ylabel, legend , savefig

nyc_temp = [26,25,25,29,32,33,31,31]
nellore_temp = [30,31,34,38,37,34,32,31]

time = ['6 AM','9 AM','12 PM','3 PM','6 PM','9 PM','12 AM','3 AM']


plot(time, nyc_temp, time, nellore_temp)
title('Daily temperature in NYC & Nellore')
xlabel('Time')
ylabel('Temperature')
legend(['NYC','Nellore'])

show()