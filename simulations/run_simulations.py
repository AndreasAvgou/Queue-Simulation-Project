from simulator import simulate_mm1

if __name__=="__main__":
    for rho in [0.1,0.5,0.9]:
        result = simulate_mm1(lmbda=rho, mu=1.0, sim_time=50000, random_seed=42)
        print(f"Rho={rho}: {result}")
