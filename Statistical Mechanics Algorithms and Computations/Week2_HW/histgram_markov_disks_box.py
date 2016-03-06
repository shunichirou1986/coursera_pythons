import random, pylab

def MC_discs_box(sigma):
    L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
    
    sigma_sq = sigma ** 2
    delta = 0.1
    n_steps = 2000000
    for steps in range(n_steps):
        a = random.choice(L)
        print type(a)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
    return L


#Compute and Plot histgram
N = 4
histo_data = []
sigma = 0.1197
n_runs = 1000


for run in range(n_runs):
    pos = MC_discs_box(sigma)
    for k in range(N): histo_data.append(pos[k][0])
    print run
pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('The histgram of x-positions by Markov Chain algorithm')
pylab.grid()
pylab.savefig('Markov Chain_histo.png')
pylab.show()
