'''
@author Sai
File name: HW05-01.py
Date created: 7/22/2019
Date last modified: 7/22/2019
Python Version: 3.1
This file reads the student data that differentiates sports and others from files and prepares the venn diagram 
'''

import csv
import os
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet




def read_csv(filename):
    football = []
    others = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                football.append(int(row[0]))
            if row[2] == '1':
                others.append(int(row[0]))
    return football, others

def draw_venn(sets):
    venn2(subsets=sets,set_labels=('Sports','Others'))
    plt.show()

if __name__ == "__main__":
    football,others = read_csv(os.path.dirname(os.path.realpath(__file__)) + "\\sports.csv")
    s1 = FiniteSet(*football)
    s2 = FiniteSet(*others)
    draw_venn([s1, s2])