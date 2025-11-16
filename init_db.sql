CREATE TABLE IF NOT EXISTS mm1_results (
    id SERIAL PRIMARY KEY,
    rho FLOAT,
    sim_L FLOAT,
    sim_W FLOAT,
    theory_L FLOAT,
    theory_W FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS mm1k_results (
    id SERIAL PRIMARY KEY,
    lambda FLOAT,
    mu FLOAT,
    K INTEGER,
    sim_P_loss FLOAT,
    sim_L FLOAT,
    theory_P_loss FLOAT,
    theory_L FLOAT,
    theory_rho_util FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
