# Queue Simulation Project (M/M/1 & M/M/1/K)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Docker](https://img.shields.io/badge/docker-ready-green)

## Project Overview

This project simulates **M/M/1** and **M/M/1/K queues** using an **event-driven simulation engine**, compares results with theory, and stores data in **PostgreSQL**. Includes **Streamlit dashboard** and **Airflow DAGs**.

## Queueing Theory

### M/M/1 Queue

- Traffic intensity: $$\\rho = \\frac{\\lambda}{\\mu}$$
- Avg number in system: $$L = \\frac{\\rho}{1-\\rho}$$
- Avg number in queue: $$L_q = \\frac{\\rho^2}{1-\\rho}$$
- Avg time in system: $$W = \\frac{1}{\\mu-\\lambda}$$
- Avg waiting time: $$W_q = \\frac{\\rho}{\\mu-\\lambda}$$

### M/M/1/K Queue

- Blocking probability (ρ≠1): $$P_{loss} = \\frac{(1-\\rho)\\rho^K}{1-\\rho^{K+1}}$$
- Effective arrival rate: $$\\lambda_{eff} = \\lambda (1-P_{loss})$$
- Avg number in system: $$L = \\sum_{n=0}^K n P_n$$
- Avg time in system: $$W = \\frac{L}{\\lambda_{eff}}$$
- Server utilization: $$\\rho_{util} = 1-P_0$$
