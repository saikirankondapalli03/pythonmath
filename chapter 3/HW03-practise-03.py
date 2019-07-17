from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes
    
if __name__ == '__main__':
    scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
    modes = calculate_mode(scores)
    print('The mode(s) of the list of numbers are:')
    for mode in modes:
        print(mode)


import numpy as np

a = np.array([5, 1, 9, 3, 14, 9,7])
p = np.percentile(a, 25) # return 50th percentile, e.g median.
print(p)


x=1.243433
s=str(x).split('.')
i=int(s[0])
d=int(s[1])/10
print(d)