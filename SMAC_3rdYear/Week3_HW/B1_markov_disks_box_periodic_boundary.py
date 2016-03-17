import random,math,pylab


def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

def show_conf(M, sigma, title, fname):
    pylab.axes()
    pylab.clf()
    for [x, y] in M:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius = sigma,  fc = 'r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
#    pylab.show()


L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
N=4
eta = 0.70
sigma =math.sqrt(eta/(N*math.pi))
sigma_sq = sigma ** 2
delta = 0.1
n_steps = 10000


for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b,c) for c in L if c != a)
#    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma

    if not (min_dist < 2.0 * sigma):
        #accepted move
        b[0] = b[0] % 1.0
        b[1] = b[1] % 1.0
        a[:] = b
print L
show_conf(L,sigma,"Markov disks periodic boundary","My_markov_disks_periodic_boundary.png")