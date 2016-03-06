import random, math,pylab

def Vol1_s(radius,dimension):
    return (radius ** dimension) *math.pi ** (dimension /2.0)/math.gamma(dimension /2.0+1.0)

vol1_data=[]
dimension_data=[]


for dimension in range(1,200):
    vol1_data.append(Vol1_s(1,dimension))
    dimension_data.append(dimension)
    
print vol1_data

pylab.gca().set_yscale('log')
pylab.xlabel('dimension', fontsize=16)
pylab.ylabel('volume', fontsize=16)
pylab.plot(dimension_data, vol1_data, linewidth=1.5, color='r')
pylab.title('The volume of hypersphere for dimension 1-200',fontsize=16)
pylab.savefig('volume_of_hypersphere_by_dimension1-200.png')
pylab.show()

print "Vol1_s(5):%s"% Vol1_s(1,5)
print "Vol1_s(20):%s"% Vol1_s(1,20)
print "Vol1_s(200):%s"% Vol1_s(1,200)
