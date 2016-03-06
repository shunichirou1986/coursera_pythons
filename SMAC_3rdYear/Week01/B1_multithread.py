import random, math, pylab
import multiprocessing as mp

def markov_pi(N, delta):
    x, y = 1.0, 1.0
    n_hits = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0: n_hits += 1
    return n_hits

def estimate_sigma(queue,n_trials_sub,delta_sub,n_runs_sub):
    for run in range(n_runs_sub):
        pi_est_sub = 4.0 * markov_pi(n_trials_sub,delta)/float(n_trials)
        sigma_sub += (pi_est - math.pi)**2
    queue.put( sigma_sub)

n_runs = 1000
for delta in[0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]:
    print 'delta = ',delta
    n_trials_list = []
    sigmas = []
    for poweroftwo in range(4, 13):
        n_trials = 2 ** poweroftwo
        queue = mp.Queue()
        sigma = 0.0
        n1,n2,n3,n4 = float(n_trials)/4,float(n_trials)/4,float(n_trials)/4,float(n_trials)/4
        jobs = [
        mp.Process(target=estimate_sigma, args=(queue,n1,delta,n_runs)),
        mp.Process(target=estimate_sigma, args=(queue,n2,delta,n_runs)),
        mp.Process(target=estimate_sigma, args=(queue,n3,delta,n_runs)),
        mp.Process(target=estimate_sigma, args=(queue,n4,delta,n_runs)),
        ]
        for j in jobs:
            j.start()
        for j in jobs:
            j.join()
        total = 0
        for i in range(4):
            total += queue.get()
        sigmas.append(math.sqrt(float(total)/(float(n_runs))))
        n_trials_list.append(n_trials)

    pylab.plot(n_trials_list, sigmas, 'o', ms = 8, label = '$\delta = $' + str(delta))

pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel('number of trials')
pylab.ylabel('root mean square deviation')
pylab.plot([10,10000],[1.644 / math.sqrt(10.0), 1.644 / math.sqrt(10000.0)], label = 'direct')
pylab.title('Markov-chain sampling of pi: root mean square deviation vs. n_trials')
pylab.legend(loc='upper right')
pylab.savefig('markov_sampling_rms_deviation_more_n_runs.png')
pylab.show()