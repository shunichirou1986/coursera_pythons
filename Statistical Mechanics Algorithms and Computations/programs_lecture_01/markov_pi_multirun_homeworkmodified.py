import random,math,pylab 

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    # n_hits = 0
    n_accept = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            n_accept += 1
        # if x**2 + y**2 < 1.0: n_hits += 1
    return n_accept

n_trials = 10000
acceptance_ratio_list500 = []
acceptance_ratio_list1000 = []
delta_list = []

n_runs = 500
acceptance_ratio = 0
delta = 0.1

while delta < 5.0 :
    for run in range(n_runs):
        acceptance_ratio = markov_pi(n_trials, delta) / float(n_trials)
        # print 4.0 * acceptance_ratio
    acceptance_ratio_list500.append(acceptance_ratio)
    delta_list.append(delta)
    print acceptance_ratio
    print delta
    delta += 0.1


n_runs = 1000
acceptance_ratio = 0
delta = 0.1
while delta < 5.0 :
    for run in range(n_runs):
        acceptance_ratio = markov_pi(n_trials, delta) / float(n_trials)
        # print 4.0 * acceptance_ratio
    acceptance_ratio_list1000.append(acceptance_ratio)
    #delta_list.append(delta)
    print acceptance_ratio
    print delta
    delta += 0.1
    
pylab.plot(delta_list, acceptance_ratio_list500,  'o')

pylab.plot(delta_list, acceptance_ratio_list1000,  'x')

#pylab.gca().set_xscale('log')
#pylab.gca().set_yscale('log')
pylab.ylabel('acceptance_ratio')
pylab.xlabel('$\delta$')
pylab.title('acceptance_ratio vs delta n_runs=500&1000')
pylab.savefig('markov_pi_multirun_nruns=500and1000.png')
pylab.show()

    
    
