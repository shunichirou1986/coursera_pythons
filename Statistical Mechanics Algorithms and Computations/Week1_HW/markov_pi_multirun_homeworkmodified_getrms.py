import random,math,pylab 

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            
        if x**2 + y**2 < 1.0: n_hits += 1
       
    return n_hits

n_trials = 10000
sigma_list500 = []
sigma_list1000 = []
delta_list = []

n_runs = 1000
delta = 0.1
sigma = 0.0

while delta < 5.0 :
    sigma = 0.0
    for run in range(n_runs):
        pi_est500 = 4.0 * markov_pi(n_trials, delta) / float(n_trials)
        sigma += (pi_est500 - math.pi ) **2
        
    sigma_list500.append(math.sqrt(sigma/(n_runs)))
    delta_list.append(delta)
    print delta,pi_est500
    delta += 0.1




pylab.plot(delta_list, sigma_list500,  'o')

pylab.ylabel('RMS error')
pylab.xlabel('$\delta$')
pylab.title('RMS vs delta')
pylab.savefig('markov_pi_multirun_nruns_RMS.png')
pylab.show()

    
    
