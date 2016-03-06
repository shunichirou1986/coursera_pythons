import math
import random

def Vol1_s(dimension):
    return math.pi ** (dimension /2.0)/math.gamma(dimension /2.0+1.0)

dimension_max = 20
n_trials = 10000000

print n_trials
print "dimension |estimation of Vol1_s(d) | Vol1_s(d) (exact)|n_hits"
for dimension in range(1,dimension_max +1):
    n_reject = 0
    for trials in range(n_trials):
        hyperradius_square = 0.0
        for d in range(dimension):
            hyperradius_square += random.uniform(-1.0,1.0) ** 2
            if hyperradius_square > 1.0:
                n_reject += 1
                break
    n_accept = n_trials - n_reject
    volume = 2.0 ** dimension * n_accept /float(n_trials)
    if n_accept >0 : print dimension,volume , Vol1_s(dimension),n_accept
    else:
        print dimension ,'no sample' , Vol1_s(dimension)
 
    