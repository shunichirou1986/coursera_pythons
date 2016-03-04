import random
N = 20 ;position = 0
p = random.uniform(0.01, 0.99)
for iter in range(1000000):
    if random.uniform < p: 
        position = (position + 1) % N
    print position