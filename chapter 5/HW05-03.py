'''
@author Sai
File name: HW05-02.py
Date created: 7/22/2019
Date last modified: 7/22/2019
Python Version: 3.1
This file is all about proof of law of large numbers in python 
for law of large numbers please refer to 
How Many Tosses Before You Run Out of Money?
'''

import random

def draw_venn(sets):
    venn2(subsets=sets,set_labels=('Sports','Others'))
    plt.show()

def roll():
    heads_trials= ['heads','tails']
    return random.choice(heads_trials)

if __name__ == "__main__":
    try:
        input_val = int(input("Enter your starting amount: "))
        l = 0 ;
        coin_tosses= 0; 
        while input_val >= 0:
            heads_trails = roll()
            if heads_trails == 'heads':
                input_val = input_val + 1.0
                print(f"{heads_trails} Current amount: {input_val}")
            elif heads_trails == 'tails':
                input_val = input_val - 1.50
                print(f"{heads_trails} Current amount: {input_val}")
            coin_tosses +=1
        print(f"Game over :( Current amount: {input_val}. Coin tosses: {coin_tosses}")
    except ValueError as ve:
        print(f"error is {ve}")