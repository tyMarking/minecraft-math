import numpy as np
from scipy.stats import binom, uniform

""" GENERAL MINECRAFT CONSTANTS """
RANDOM_TICK_RATE = 3 # 3/tick
# SUBCHUNK_SIZE = 4096
SUBCHUNK_SIZE = 4
# TICK_RATE = 20 # 20/s
TICK_RATE = 20

""" KELP CONSTANTS """
KELP_GROWTH_CHANCE = 0.14 # 0.14/random tick
MAX_GROWTHS = 24


#harvest_time in seconds
def get_kelp_production(harvest_time, max_harvest_height):
    
    #cap kelp return to harvest_height
    
    ticks = harvest_time*TICK_RATE

    #use binomial theorem to calc prob of the height a kelp to grow to capped at harvest height
    # r successes in n successive independent trials with probability p, p fixed all independent
    
    #distribution of number of random ticks a kelp recieves
    n = RANDOM_TICK_RATE*ticks
    p = 1/SUBCHUNK_SIZE
    r_space = list(range(0, n+1)) # Cap at a maximum number of random ticks?
    random_ticks_dist = np.asarray([binom.pmf(r,n,p) for r in r_space])
    #(random_ticks,) 
    #growth attempts dist with n = number of random ticks, r = growth attempts
    n_range = list(range(0, RANDOM_TICK_RATE*ticks+1))
    p = KELP_GROWTH_CHANCE
    r_space = list(range(0, MAX_GROWTHS)) # Cap at a maximum number of random ticks?
    growths_per_random_ticks_dist = np.asarray([[binom.pmf(r,n,p) for r in r_space] for n in n_range])
    #(random_ticks, growth attempts)


    growths_dist = np.matmul(random_ticks_dist, growths_per_random_ticks_dist)
    # max growth height from kelp age
    is_age_capped_dist = np.asarray([(i)/MAX_GROWTHS for i in range(1,MAX_GROWTHS+1)])
    # print(random_ticks_dist)
    # print(growth_attempts_dist)
    print(growths_dist)
    print(is_age_capped_dist)
    # print(sum(growths_dist[:max_harvest_height+1]))
    # print(random_ticks_dist.shape)
    # print(growth_attempts_dist.shape)
    # print(growths_dist.shape)

def plot_harvest_rate_per_height():
    pass

if __name__ == "__main__":
    get_kelp_production(10, 10)
    # plot_harvest_rate_per_height()