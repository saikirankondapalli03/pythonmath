'''
@author Sai
File name: HW02-04.py
Date created: 4/16/2019
Date last modified: 4/16/2019
Python Version: 3.1
This file is for tracking expenditure with a bar graph
'''
import matplotlib.pyplot as plt
import sys

def create_bar_chart(data, labels):
    # Number of bars
    num_bars = len(data)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Expenditure')
    plt.ylabel('Categories')
    plt.title('Weekly expenditure')
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()

if __name__ == '__main__':
    try:
      no_of_trajectories =  int(input('Enter the number of categories: '))
      i =1 
      category_list = []
      expenditure_list= []
      while i <= no_of_trajectories:
        category = input(f'Enter the category: ')
        expenditure = float(input(f'Expenditure: '))
        category_list.append(category)
        expenditure_list.append(expenditure)
        i += 1
      create_bar_chart(expenditure_list, category_list)         
    except ValueError as ve:
      print(f'You entered an invalid input and error is {ve}')
