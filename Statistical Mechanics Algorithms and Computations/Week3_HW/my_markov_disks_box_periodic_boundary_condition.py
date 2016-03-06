import random,math,pylab,os

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  (d_x**2 + d_y**2)


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

#########################Constants
N = 256
k = int(math.sqrt(N))
eta = 0.42
sigma = math.sqrt(eta/N/math.pi)
delta = 0.023
n_steps = 2000
accept_ratio = 0.0
intermediate_filename = 'filename'
#########################Read File Initial
filename = 'disk_configuration_forMC.txt'
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    L = []
    x = 0
    y = 0
    ini_x = 0.0
    ini_y = 0.0
    for x in range(0,k):
        for y in range(0, k):
            print 'x',x,'y',y
            ini_x = float(x)/float(k)
            ini_y = float(y)/float(k)
            print 'ini_x',ini_x,'ini_y',ini_y
            L.append([ini_x,ini_y])
        
    print 'starting from scratch' , L


for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b,c) for c in L if c != a)
    if (min_dist > 4.0 * sigma**2): 
        a[:] = [b[0]%1.0,b[1]%1.0]
        accept_ratio += 1
    if steps %1000 == 0:
        print steps
#    	intermediate_filename = 'intermediate'+ str(steps)
#    	show_conf(L,sigma,'intermediate_configuration'+str(steps),intermediate_filename)
print 'final configuration',L ,'accept ratio',accept_ratio/n_steps

glaf_name = 'markov_disk N=' +str(N)+'eta='+str(eta)
show_conf(L, sigma, glaf_name, 'MC_DisksFinalCoodinate.png')

f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()