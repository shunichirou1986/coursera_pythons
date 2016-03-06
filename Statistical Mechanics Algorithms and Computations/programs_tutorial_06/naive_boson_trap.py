import math

Energy = [0.0] + [1.0] * 3 + [2.0] * 6 + [3.0] * 10 + [4.0] * 15
beta = 1.0
n_states = 0#
# Part one
#
L = range(10)
for k in range(10):
    print L
    L = L[3:] + L[:3]
print
#
# Part two 
#
K = range(10)
for i in range(10):
    print K
    dummy = K.pop()
    K = [dummy] + K
print
#
# Part three
#
J = range(10)
for i in range(10):
    print K
    dummy = K.pop(0)
    K = K + [dummy]
print
#
# Part four
#
I = range(10)
weight = sum(a ** 2 for a in I)
Z = 0.0
N0_mean = 0.0
E_mean = 0.0
for s_0 in range(35):
    for s_1 in range(s_0, 35):
        for s_2 in range(s_1, 35):
            for s_3 in range(s_2, 35):
                for s_4 in range(s_3, 35):
                    n_states += 1
                    state = [s_0, s_1, s_2, s_3, s_4]
                    E = sum(Energy[s] for s in state)
                    Z += math.exp(-beta * E)
                    E_mean += E * math.exp(-beta * E)
                    N0_mean += state.count(0) *\
                               math.exp(-beta * E)
print n_states, Z, E_mean / Z / 5.0, N0_mean / Z / 5.0
