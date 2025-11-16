# Queue Simulation Project (M/M/1 & M/M/1/K)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Docker](https://img.shields.io/badge/docker-ready-green)

## Project Overview

The goal of this project is to simulate queueing systems under various traffic loads, compare simulation results with theoretical values, and store them in a database.  
Streamlit provides an interactive dashboard to visualize metrics like system utilization, average waiting time, and maximum queue length.

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

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Database Schema](#database-schema)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Technologies Used

- **Python** (Simulation engine, data processing)
- **PostgreSQL** (Database for storing simulation results)
- **Docker & Docker Compose** (Containerization and orchestration)
- **Airflow** (Automating scheduled simulations)
- **Streamlit** (Dashboard visualization)

---

## Features

- Simulates M/M/1 and M/M/1/K queues
- Compares simulation with theoretical results
- Stores results in PostgreSQL
- Interactive dashboard with Streamlit
- Airflow DAGs for scheduled simulations
- Easy deployment via Docker Compose

---

## Directory Structure

- **`Dockerfile`**: Dockerfile for building the application container  
- **`docker-compose.yml`**: Docker Compose configuration for all services  
- **`dags/`**: Airflow DAGs folder  
  - **`queue_sim_dynamic_dag.py`**: DAG that triggers simulations and updates DB  
- **`simulations/`**: Python code for running queue simulations  
  - **`simulator.py`**: Core event-driven simulation functions  
- **`app_dashboard.py`**: Streamlit dashboard for visualizing results  
- **`data/`**: Folder to store CSV exports and intermediate results  
- **`outputs/plots/`**: Folder for generated plots  
- **`outputs/data/`**: Folder for simulation CSV files  

---

## Installation and Setup

### Prerequisites

- **Docker**: For containerization.
- **Docker Compose**: For managing multi-container setups. 
- (Optional) pgAdmin or any PostgreSQL client for inspecting the database

### Setup Instructions

1. **Clone the repository**  
  ```bash
  git clone https://github.com/AndreasAvgou/Queue-Simulation-Project.git
  cd queue-simulation-project
  ```

2. **Build and Start the Containers**

   To build and run the containers for the application, run the following command:

   ```bash
   docker-compose up --build

3. **Access pgAdmin4**

- Open a browser and navigate to [http://localhost:5050](http://localhost:5050).
- Login with the credentials provided in the `docker-compose.yml` file.

## Running the Application

Airflow DAGs automatically trigger simulations and update the database.  
Access Airflow UI: [http://localhost:8080](http://localhost:8080)

Streamlit Dashboard reads the database and shows plots:  [http://localhost:8501](http://localhost:8501)

Manually run simulation scripts inside the container:

```bash
docker exec -it <container_name> python simulations/simulator.py
