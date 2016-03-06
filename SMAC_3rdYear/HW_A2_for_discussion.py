#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      shunichirou
#
# Created:     06/03/2016
# Copyright:   (c) shunichirou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random, math, pylab

def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits

def main():
    n_runs = 500
    n_trials_list = []
    sigmasqs = []

    n_trials = 100
    sigmasq = 0.0
    for run in range(n_runs):
        pi_est = 4.0 * direct_pi(n_trials) / float(n_trials)
        sigmasq += (pi_est - math.pi) ** 2
    error = math.sqrt(sigmasq/(n_runs))
    print "error" ,"error/1.644*10",error,error/1.644*10


if __name__ == '__main__':
    main()
