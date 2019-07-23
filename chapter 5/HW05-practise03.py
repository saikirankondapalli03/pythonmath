import random


# 0 - 2/3 heads 2/3 - 1 tails
#
def toss():
# 0 -> Heads, 1-> Tails
    x= random.random() 
    if x < 2/3:
        return 0 #heads
    else:
        return 1 #tails

toss()

