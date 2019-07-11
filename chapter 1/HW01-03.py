'''
@author Sai
File name: HW01-03.py
Date created: 7/10/2019
Date last modified: 7/10/2019
Python Version: 3.1
This file is for enhanced unit converter
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kg to Pounds')
    print('4. Centigrade to fareinheit')


def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))

def kg_pounds():
    kgweight = float(input('Enter weight in kgs: '))
    usweight = (float(kgweight) * 2.2046)
    print(f'weight of {kgweight} in kgs is same as {usweight} lbs')

def centi_farein():
    centi = float(input('Enter temperature in centigrade: '))
    farenheit = (float(centi) *9/5) + 32
    print(f'{centi} degree celsius is same as {farenheit} fareinheit')

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        kg_pounds()
    if choice == '4':
        centi_farein()
