'''
@author Sai
File name: HW03-04.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is for read file and calculate percentile
Note: (Still showing wrong value percentile even though the code is correct)

'''

import csv
import matplotlib.pyplot as plt

def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()

def read_csv(filename):
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            numbers.append(int(row[0]))
        return numbers

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

def calculate_percentile(numbers,percentile):
    size_of_numbers= len(numbers)
    data = sorted(numbers)
    i = (size_of_numbers * percentile)/100 + 0.5
    if i.is_integer():
        return data[int(i)]
    else:
        str_val= str(i)
        int_part= int(str_val.split('.')[0])
        dec_part= int(str_val.split('.')[1])
        print(int_part)
        print(dec_part)
        return (1-dec_part)*data[int_part] + dec_part*data[int_part+1]


import os 

if __name__ == '__main__':
    data = read_csv(os.path.dirname(os.path.realpath(__file__))+'\\numbers-04.csv')
    percentile = float(input('Please enter the percentile you want to check: '))
    print(f"{percentile}")
    result = calculate_percentile(data,percentile)
    print(f"number corresponding to specific percentile is {result}")

    '''
    print('Mean: {0}'.format(calculate_mean(data)))
    print('Median: {0}'.format(calculate_median(data)))
    print('Mode: {0}'.format(calculate_mode(data)))
    var = calculate_variance(data)
    print('Variance :{0}'.format(var))
    print('Standard Deviation :{0}'.format(var**(0.5)))
    '''
    
