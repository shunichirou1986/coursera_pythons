import random
import multiprocessing as mp

def markov_disk(M,delta,sigma):

    a = random.choice(M)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in M if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist < 4.0 * sigma ** 2):
        a[:] = b
    return M

def subcalc(queue,i,x_vec,delta,sigma):
    subtotal = 0
    x_vec_sub = markov_disk(x_vec,delta,sigma)
    queue.put(x_vec_sub)

sigma = 0.15
delta = 0.1
n_runs = 10000000
del_xy = 0.05

conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}

#x_vec initialization
x_vec = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
x_vec_all = []

queue = mp.Queue()
ps =[
    mp.Process(target=subcalc, args=(queue, 0,x_vec,delta,sigma)),
    mp.Process(target=subcalc, args=(queue, 1,x_vec,delta,sigma)),
    mp.Process(target=subcalc, args=(queue, 2,x_vec,delta,sigma)),
    mp.Process(target=subcalc, args=(queue, 3,x_vec,delta,sigma)),
    mp.Process(target=subcalc, args=(queue, 4,x_vec,delta,sigma)),
    mp.Process(target=subcalc, args=(queue, 5,x_vec,delta,sigma)),
    mp.Process(target=subcalc, args=(queue, 6,x_vec,delta,sigma)),
    mp.Process(target=subcalc, args=(queue, 7,x_vec,delta,sigma))
]


for run in range(n_runs/8):
    for p in ps:
        p.start()

    for i in range(8):
        x_vec_all.append(queue.get())

    for x_vec in x_vec_all:
        for conf in configurations:
            condition_hit = True
            for b in conf:
                condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in x_vec) < del_xy
                condition_hit *= condition_b
            if condition_hit:
                hits[conf] += 1

for a in hits:
    print a, hits[a]