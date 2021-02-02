from random import randint
from math import sqrt

count = 0

while True:
    x = randint(1,int(1e6)) ** 2
    x = sqrt(x)
    count += 1
    
    print(count)

# 300000 ops per second