import random
N = 20; position = 0
for t in range(100000):
    if random.uniform(0.0, 1.0) < 0.5:
        position = (position + 1) % N
    elif random.uniform(0.0, 1.0) > 0.5:
        position = (position - 1) % N
    print position