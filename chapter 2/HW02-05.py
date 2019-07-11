'''
@author Sai
File name: HW02-05.py
Date created: 4/16/2019
Date last modified: 4/16/2019
Python Version: 3.1
This file is for plotting consecutive fibonacci ratio
'''
from pylab import plot,show,title, xlabel, ylabel, legend , savefig
import sys




def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(1,n-1):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series

def get_first_n_natural_numbers(n):
    return  [i+1 for i in range(n)]


if __name__ == '__main__':
    try:
        number =  int(input('Enter the number of fibonacci numbers: '))
        numbers = fibo(number)
        #print(numbers)  
        #print(numbers[1:])     
        result = [x1/x2 for (x1, x2) in zip(numbers, numbers[1:])]
        result.insert(0,1.0)
        print(result)
        first_100_numbers= get_first_n_natural_numbers(number)
        plot(first_100_numbers,result)
        xlabel('numbers')
        ylabel('ratios')
        title('Ratio between consecutive fibonacci numbers')
        show()
    except ValueError as ve:
      print(f'You entered an invalid input and error is {ve}')
