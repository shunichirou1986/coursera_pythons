import math, pylab

n_states = 40
Energies = [0.5 + i for i in range(n_states)]
dx = 0.2
grid_x = [i * dx for i in range(-25, 26)]
psi = {}
for x in grid_x:
    psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]  # ground state
    psi[x].append(math.sqrt(2.0) * x * psi[x][0])         # first excited state
    # other excited states (through recursion):
    for n in range(2, n_states):
        psi[x].append(math.sqrt(2.0 / n) * x * psi[x][n - 1] -
                      math.sqrt((n - 1.0) / n) * psi[x][n - 2])
beta = 2.0
Z = sum(math.exp(-beta * Energies[k]) for k in range(n_states))
print beta, 'beta'
print Z, ' Z from \sum_n exp(-beta E_n)'
print 1.0 / (2.0 * math.sinh(beta/2)), ' Z (exact)'
Z_trace = 0.0
x_values = []
y_values = []
for x in grid_x:
    rho_xx = sum(math.exp(-beta * Energies[i]) * psi[x][i] ** 2 for i in range(n_states))
    Z_trace += rho_xx * dx
    x_values.append(x)
    y_values.append(rho_xx/Z)
print Z_trace, ' Z (from trace over density matrix)'
pylab.title('Harmonic oscillator $ \\beta = 2$ ')
pylab.xlabel('x')
pylab.ylabel('$\pi(x)$')
pylab.plot(x_values, y_values, label='harmonic_wavefunctions')
pylab.legend()
pylab.axis([-4.0, 4.0, 0.0, 0.6])
pylab.savefig('density_x_harm_wave.png')
pylab.show()