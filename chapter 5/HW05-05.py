'''
@author Sai
File name: HW05-05.py
Date created: 7/22/2019
Date last modified: 7/22/2019
Python Version: 3.1
this file accepts the radius as input and computes area of circle and estimated area of circle depending on darts
'''
import math,random

def random_value_circle(radius):
    return random.uniform(0, 2*radius)

if __name__ == "__main__":
    radius = int(input("Radius: "))
    val = math.pi
    area = val* (radius**2)
    print(f"Original Area: {radius}")
    #Radius: 2
    #Area: 12.566370614359172, Estimated (1000 darts): 12.576
    #Area: 12.566370614359172, Estimated (100000 darts): 12.58176
    #Area: 12.566370614359172, Estimated (1000000 darts): 12.560128
    # 1000 darts => for loop 1001 darts => for every loop use random.uniform dart => get the value => 
    inside_circle= 0 
    outside_circle= 0 
    list_of_experiments = [1000,100000,1000000]
    #list_of_experiments = [10] check with sample as 10 
    for each_experiment in list_of_experiments:
        for i in range(1,each_experiment+1):
            rand_val= random_value_circle(radius)
            if rand_val > radius:
                outside_circle += 1
            elif rand_val <= radius:
                inside_circle += 1
        print(f"darts inside the circle or on the circle is {inside_circle} and darts outside circle is {outside_circle}")
        net_count_inside_circle = (inside_circle)/(outside_circle+inside_circle)
        print(f"net count inside the circle is {net_count_inside_circle}")
        net_area = net_count_inside_circle * area
        print(f"Area: {area}, Estimated ({each_experiment} darts): {net_area} ")
            



    
    
    


