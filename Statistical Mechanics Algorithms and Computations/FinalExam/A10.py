import random, math

sigma = 0.18
for t in range(1000):
    L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
    while True:
        a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
        min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L)
        if min_dist > 2.0 * sigma:
            L.append(a)
            print len(L)
            if len(L) == 4: break
    print L