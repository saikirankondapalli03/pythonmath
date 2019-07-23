'''
@author Sai
File name: HW05-02.py
Date created: 7/22/2019
Date last modified: 7/22/2019
Python Version: 3.1
This file is all about proof of law of large numbers in python 
for law of large numbers please refer to 
a) https://en.wikipedia.org/wiki/Law_of_large_numbers
b) https://en.wikipedia.org/wiki/Law_of_large_numbers#/media/File:Lawoflargenumbers.svg 
'''

import random
import symbol

def roll():
    return random.randint(1, 6)

def calculate_avg(no_of_trials):
    i =0 
    new_list= []
    for i in range(1,no_of_trials+1):
        val= roll()
        new_list.append(val)
    avg = sum(new_list)/len(new_list)
    return avg

from pylab import plot,show,title, xlabel, ylabel, legend , savefig


if __name__ == "__main__":
    input_trials = [10,100,1000,10000,100000,500000]
    output_trials = []
    for input in input_trials:
        result= calculate_avg(input)
        output_trials.append(result)
    print(input_trials)
    print(output_trials)
    #we already know that theoritical mean is 3.5 (as per the calculation in page no 143 from the textbook ) 
    #So for any number of trials , it is always close to 3.5
    #So , now given that input_trials = [10,100,1000,10000,100000,500000] is of length 6 , create input of length 6 in which each element is 3.5 
    theoritical_mean_trials = [3.5,3.5,3.5,3.5,3.5,3.5] 
    plot(input_trials, output_trials, input_trials, theoritical_mean_trials )
    title('Average dice roll by number of trials')
    xlabel('Number of trials')
    ylabel('Observed averages')
    legend(['Theotrical Mean','Observed averages'])

    show()



