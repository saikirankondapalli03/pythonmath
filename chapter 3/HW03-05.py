'''
@author Sai
File name: HW03-04.py
Date created: 7/16/2019
Date last modified: 7/16/2019
Python Version: 3.1
This file is for read file and display frequency of numbers for the range of input mentioned. calculate range and assign frequency and display
'''

import csv

def read_csv(filename):
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            numbers.append(int(row[0]))
        return numbers



def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)
    # Width of each class
    width = (high - low)/n
    classes = []
    a = low
    b = low + width
    classes = []
    while a < (high-width):
        classes.append((a, b))
        a = b
        b = a + width
    # The last class may be of a size that is less than width
    classes.append((a, high+1))
    return classes

import os
from collections import defaultdict
from prettytable import PrettyTable

if __name__ == '__main__':
    data = read_csv(os.path.dirname(os.path.realpath(__file__))+'\\numbers-05.csv')
    result = create_classes(data,4)
    print(f"number corresponding to specific percentile is {result}")
    map = defaultdict(int)
    for eachtuple in result:
        leftside= eachtuple[0]
        rightside= eachtuple[1]
        for eachValue in sorted(data): 
            if eachValue >= leftside and eachValue < rightside:
                map[eachtuple] += 1
    table = PrettyTable()
    table.field_names = ["Grade","Frequency"]
    for key,value in map.items():
        table.add_row([f"{key[0]} - {key[1]}",value])
    print(f"summary \n {table}")
            
            



        
        

