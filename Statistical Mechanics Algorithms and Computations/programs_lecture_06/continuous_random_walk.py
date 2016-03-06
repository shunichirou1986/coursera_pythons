import math, random
import pylab
beta = 4.0
N = 8
sigma = math.sqrt(beta / N)
x = [0.0]
for k in range(N - 1):
    x.append(random.gauss(x[-1], sigma))
print x
for i in range(0,N):
    pylab.scatter(x[i],i)
pylab.yrange(0,N)
pylab.show()
pylab.cla()