import random
N = 20; position = 0
for iter in range(1000000):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.4: 
        position = (position - 1) % N
    elif Upsilon  > 0.6:
        position = (position + 1) % N
    print position