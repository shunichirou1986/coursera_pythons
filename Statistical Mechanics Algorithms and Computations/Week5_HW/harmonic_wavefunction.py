import math,os

def Energy(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z1(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z
    
def Z2(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

def Z3harm(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy(n, cubic, quartic)) for n in range(n_max + 1))
    return Z
    

n_max = 5.0
n_states = 40
cubic = -0.5
quartic = 0.5
beta = 2.0

Energies = [0.5 + i for i in range(n_states)]
grid_x = [i * 0.2 for i in range(-25, 26)]
psi = {}
for x in grid_x:
    psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25] #ground state
    psi[x].append(math.sqrt(2.0) * x * psi[x][0]) #first excited stage
    for n in range(2, n_states): #excited state n>2
        psi[x].append(math.sqrt(2.0 / n) * x * psi[x][n - 1] - math.sqrt((n - 1.0) / n) * psi[x][n - 2])