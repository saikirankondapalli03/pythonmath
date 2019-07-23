'''
Draw a Venn diagram for two sets
'''
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

def draw_venn(sets):
    venn2(subsets=sets)
    plt.show()

if __name__ == '__main__':
    
    s1 = FiniteSet(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
    s2 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)
    draw_venn([s1, s2])
    
    '''
    sum_final = 0 
    i=0
    while i <= 6:
        sum_final = sum_final + i* (1/100)
        i += 1
    print(sum_final)
    '''


