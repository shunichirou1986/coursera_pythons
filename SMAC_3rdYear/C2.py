import random, math

n_trials = 400000
n_hits = 0
var = 0.0
Obs_sum = 0.0
Obs_square_sum =0.0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
    Obs_sum += Obs
    Obs_square_sum += Obs * Obs
#Calculate Standard deviation <Obs^2> - <Obs>^2.
var = math.sqrt((Obs_square_sum/(float(n_trials))-Obs_sum/float(n_trials))*(Obs_sum/float(n_trials)) )
print 4.0 * n_hits / float(n_trials), var