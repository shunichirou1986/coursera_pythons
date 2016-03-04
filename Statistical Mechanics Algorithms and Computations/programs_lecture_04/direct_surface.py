import random, math,matplotlib.pyplot as plt

dimensions = 1000
nsamples = 20000
ls_radius = []

for sample in xrange(nsamples):
    R = [random.gauss(0.0, 1.0) for d in xrange(dimensions)]
    radius = math.sqrt(sum(x ** 2 for x in R))
#    print radius
    ls_radius.append(radius)
#        print [x / radius for x in R]
plt.hist(ls_radius,bins=100,histtype='step',stacked=True)
ls_radius = []


plt.show()

