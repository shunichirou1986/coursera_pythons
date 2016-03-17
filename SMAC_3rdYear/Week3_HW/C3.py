import random, math, pylab, os, cmath,sys

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)

N = 64
eta = 0.72
filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    print 'ERROR: %s is missing. Exit.' % filename
    sys.exit()

n_steps = 25000
list_eta = []
list_Psi_6 = []
while eta > 0.2:
    sigma = math.sqrt(eta / (N * math.pi))
    delta = sigma * 0.3
    tot_Psi_6 = 0.0
    for step in range(n_steps):
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta) , a[1] + random.uniform(-delta, delta)]
        min_dist = min(dist(b, c) for c in L if c != a)
        if min_dist > 2.0 * sigma:
            a[:] = [b[0] % 1.0, b[1] % 1.0]
        if step % 100 == 0:
            tot_Psi_6 += abs(Psi_6(L, sigma))
    av_Psi_6 = tot_Psi_6 / float(n_steps / 100)
    list_eta.append(eta)
    list_Psi_6.append(av_Psi_6)
    print 'eta = %f, |Psi_6| = %f' % (eta, av_Psi_6)
    eta -= 0.02

pylab.plot(list_eta, list_Psi_6, '.-')
pylab.title('Hard disks: global orientational order parameter $N=64$')
pylab.ylim(0.0, 0.8)
pylab.xlabel('$\eta$')
pylab.ylabel('$|\Psi_6|$')
pylab.savefig('plot_Psi_6.png')
pylab.show()