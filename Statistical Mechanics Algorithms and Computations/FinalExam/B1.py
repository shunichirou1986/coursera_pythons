import random
N = 20; position = 0
for t in range(100000):
    dir = random.choice([-1, 1])
    position = (position + dir) % N
    print position