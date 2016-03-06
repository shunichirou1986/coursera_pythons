m = 134456
n = 8121
k = 28411
idum = 1000

import matplotlib.pyplot as plt
y_list = []


for iteration in xrange(2000000):
    idum = (idum *  n + k) % m
    ran = idum / float(m)
    y_list.append(idum)
#    print idum, ran, iteration
plt.hist(y_list,bins=2048)
plt.show()