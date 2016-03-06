import random
import pylab


x, y = 1.0, 1.0
delta = 0.1
n_trials = 2**12
n_hits = 0
acceptance_rate = 0.0
print "delta | acceptance_rate"
for delta in [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0,5.0]:
    pylab.clf()
    circle = pylab.Circle([0.0,0.0],1.0,fill=False)
    rectangle = pylab.Rectangle(xy=[-1.0,-1.0],width=2.0,height=2.0,angle=0.0,fill=False)
    ax = pylab.axes(aspect=1.0)
    ax.add_patch(circle)
    ax.add_patch(rectangle)


    for i in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        pylab.plot(x,y,"o")
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            acceptance_rate += 1.0


        if x**2 + y**2 < 1.0: n_hits += 1
    print str(delta) +" | "+ str(acceptance_rate/float(n_trials))
    acceptance_rate = 0.0
    n_hits=0.0
    pylab.xlabel('x')
    pylab.xlim(-1.0,1.0)
    pylab.ylabel('y')
    pylab.ylim(-1.0,1.0)
    pylab.title('Markov-chain sampling of pi plotting')
    pylab.savefig('markov_pi_plot_'+str(delta)+"_.png",format="png")

 #   print 4.0 * n_hits / float(n_trials)
