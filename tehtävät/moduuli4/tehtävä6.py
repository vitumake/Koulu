import math
import random
n=0
N=int(input('Anna testattavien pistiden määrä: '))
for i in range(N):
    if pow(random.uniform(-1, 1), 2) + pow(random.uniform(-1, 1), 2) < 1:
        n+=1
print('Pi:n likiarvo on: ' + str(4*n/N))
print('Pi:n vakio math librarysta: ' + str(math.pi))