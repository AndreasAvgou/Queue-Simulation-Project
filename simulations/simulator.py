import numpy as np

def simulate_mm1(lmbda, mu, sim_time=1e5, random_seed=None):
    np.random.seed(random_seed)
    t = 0.0
    n = 0
    last_event_time = 0.0
    area_n = 0.0
    max_queue = 0
    next_arrival = np.random.exponential(1.0 / lmbda)
    next_departure = float('inf')
    arrivals, departures = [], []

    while t < sim_time:
        if next_arrival <= next_departure:
            t = next_arrival
            area_n += n*(t-last_event_time)
            last_event_time = t
            arrivals.append(t)
            if n==0: next_departure = t + np.random.exponential(1.0/mu)
            n+=1
            max_queue = max(max_queue,max(0,n-1))
            next_arrival = t + np.random.exponential(1.0/lmbda)
        else:
            t = next_departure
            area_n += n*(t-last_event_time)
            last_event_time = t
            departures.append(t)
            n-=1
            next_departure = t + np.random.exponential(1.0/mu) if n>0 else float('inf')

    matched = min(len(arrivals),len(departures))
    arrivals = np.array(arrivals[:matched])
    departures = np.array(departures[:matched])
    Ws = departures - arrivals
    W = np.mean(Ws)
    Wq = W - 1.0/mu
    L = area_n/sim_time
    Lq = L - (len(departures)/sim_time)*(1.0/mu)
    rho_est = (len(departures)*(1.0/mu))/sim_time

    return {"L":L,"Lq":Lq,"W":W,"Wq":Wq,"rho_est":rho_est,"max_queue":max_queue}
