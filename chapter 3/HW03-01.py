'''
@author Sai
File name: HW03-01.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is for enhanced find_corr_x_y
'''

import sys

def find_corr_x_y(x,y):
    if len(x) != len(y):
        print("please ensure that both x and y are of same size.")
        sys.exit()
        #sys.exit()
    n = len(x)
    # Find the sum of the products
    prod = []

    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    
    x_square = []
    
    for xi in x:
       x_square.append(xi**2)
    # Find the sum
    x_square_sum = sum(x_square)
    
    y_square=[]
    for yi in y:
       y_square.append(yi**2)
    # Find the sum
    y_square_sum = sum(y_square)
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    return correlation

import math


def find_differences(numbers):
    # Find the mean
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # Calculate the mean
    mean = s/N
    return mean

def calculate_std(numbers):
# Find the list of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    std = variance**0.5
    return std


from prettytable import PrettyTable
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x1= [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
    y1= [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]
    x2= [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
    y2= [9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]
    x3= [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
    y3= [7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]
    x4= [8.0,8.0,8.0,8.0,8.0,8.0,8.0,19.0,8.0,8.0,8.0]
    y4= [6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89]
    
    result = []
    result.append(('A',calculate_mean(x1) , calculate_std(x1),  calculate_mean(y1), calculate_std(y1), find_corr_x_y(x1,y1)))
    result.append(('B',calculate_mean(x2) , calculate_std(x2),  calculate_mean(y2), calculate_std(y2), find_corr_x_y(x2,y2)))
    result.append(('C',calculate_mean(x3) , calculate_std(x3),  calculate_mean(y3), calculate_std(y3), find_corr_x_y(x3,y3)))
    result.append(('D',calculate_mean(x4) , calculate_std(x4),  calculate_mean(y4), calculate_std(y4), find_corr_x_y(x4,y4)))
    table = PrettyTable()
    table.field_names = ["Dataset","Mean_X","Std_X","Mean_Y","Std_y","Corr"]
    for dataset,mean_x, std_x , mean_y, std_y, corr in result:
        table.add_row([dataset,mean_x, std_x , mean_y, std_y, corr])
    
    print(f"summary \n {table}")
    plt.scatter(x1,y1)    
    plt.show()
    plt.scatter(x2,y2)
    plt.show()
    plt.scatter(x3,y3)
    plt.show()
    plt.scatter(x4,y4)
    plt.show()
    

    

    