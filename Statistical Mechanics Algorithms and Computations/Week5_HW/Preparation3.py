import pylab, math

def V(x):
    pot =  x ** 2 / 2 + cubic * x ** 3 + quartic * x ** 4
    return pot

def Energy(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

cubic = -0.5
quartic = 0.5
x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
y = [V(a) for a in x]
pylab.plot(x, y,label='Anharmonic potential')

cubic = 0.0
quartic = 0.0
y = [V(a) for a in x]
pylab.title('Harmonic potential and Anharmonic potential plot(expansion around zero)')
pylab.xlabel('x')
pylab.ylabel('Potential energy')
pylab.plot(x, y, label='Harmonic potential')
pylab.legend()
pylab.axis([-4.0, 4.0, 0.0, 1.0])
pylab.savefig('Harmonic_potential_and_Anharmonic_potential_plot.png')
pylab.show()


t_l = 0.0
x_l = []
y_l = []
n = 1
delta_t_l = 0.01
while n < 11:
    del x_l [:]
    del y_l [:]
    t_l = 0.0
    while t_l <1:
        cubic = - t_l
        quartic = t_l
        x_l.append(t_l)
        y_l.append(Energy(n,cubic,quartic))
        t_l += delta_t_l
    pylab.plot(x_l, y_l, label='E_%i '%(n))
    
    n += 1
pylab.title('plot E(n) changing pertubation constant')
pylab.xlabel('pertubation constant cubic and quartic')
pylab.ylabel('E(n)')

pylab.legend()
pylab.axis([0, 0.5, -5, 40])
pylab.savefig('pertubation_interact_En_plot.png')
pylab.show()