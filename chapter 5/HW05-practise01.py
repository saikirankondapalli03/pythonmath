from sympy import FiniteSet
import random

def find_prob(target_score, max_rolls):
    die_sides = FiniteSet(1, 2, 3, 4, 5, 6)
    print(die_sides)
    # Sample space
    s = die_sides**max_rolls
    # Find the event set
    if max_rolls > 1:
        success_rolls = []
        for elem in s:
            #print(f"elem is {elem}")
            if sum(elem) == target_score:
                success_rolls.append(elem)
    else:
        if target_score > 6:
            success_rolls = []
        else:
            success_rolls = []
            for roll in die_sides:
                if roll == target_score:
                    success_rolls.append(roll)
                    #print(f"supper2 {roll}")
    print(f"success rolls {success_rolls} len is {len(success_rolls)}")
    e = FiniteSet(*success_rolls)
    # Calculate the probability of reaching target score
    print(f"E ==> {len(e)}")
    e = len(e)
    s = len(s)
    print(f"{e}/{s}")
    return e/s

if __name__ == '__main__':
    target_score = int(input('Enter the target score: '))
    max_rolls = int(input('Enter the maximum number of rolls allowed: '))
    p = find_prob(target_score, max_rolls)
    print('Probability: {0:.5f}'.format(p))