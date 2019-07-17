'''
@author Sai
File name: HW03-03.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is for read file and calculate mean,median,mode,
'''

import csv
import matplotlib.pyplot as plt
def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers


def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    # Find the median
    if N % 2 == 0:
    # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]
    return median

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

def read_csv(filename):
    numbers = []
    years = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(row[0])
            print(type(row[1]))
            years.append(float(row[1]))
        return years,numbers

def find_differences(numbers):
    # Find the mean
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff

def calculate_variance(numbers):
# Find the list of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]


import os 
from pylab import plot,show,title, xlabel, ylabel, legend , savefig
import sys



if __name__ == '__main__':
    data,year = read_csv(os.path.dirname(os.path.realpath(__file__))+'\\WWDI-USA_SP_POP_TOTL.csv')
    xdiff = [data[n-1]-data[n] for n in range(1,len(data))]
    ans= [0]
    ans.extend(xdiff)
    print('Mean: {0}'.format(calculate_mean(xdiff)))
    print('Median: {0}'.format(calculate_median(xdiff)))
    print('Mode: {0}'.format(calculate_mode(xdiff)))
    var = calculate_variance(xdiff)
    print('Variance :{0}'.format(var))
    print('Standard Deviation :{0}'.format(var**(0.5)))
    print(f"Years: {len(year)}")
    print(f"Data: {len(ans)}")
    plot(year,ans)
    xlabel('years')
    ylabel('Differences of populations over years')
    title('Differences of populations over years')
    show()
    
    
