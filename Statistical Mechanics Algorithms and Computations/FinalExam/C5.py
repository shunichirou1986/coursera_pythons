import random, math,pylab
N = 20; position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = [] 
for iter in range(1000000):
    dir = random.choice([-1, 1])
    new_position = (position + dir) % N
    if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]: 
        position = new_position
    pos_list.append(position)
pylab.hist(pos_list, bins=100, normed=True)
pylab.xlabel('position')
pylab.ylabel('frequency')
pylab.title('The histgram of position on N20ring')
pylab.grid()
pylab.savefig('FinalExam_C5.png')
pylab.show()