import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from psycopg2.extras import RealDictCursor

# --- Streamlit App Title ---
st.title("Queue Simulation Dashboard")

# --- Queue Type Selection ---
queue_type = st.selectbox("Select Queue Type", ["M/M/1", "M/M/1/K"])
st.write(f"Selected Queue: {queue_type}")

# --- Database Connection ---
DB_HOST = "postgres"
DB_NAME = "queue_sim"
DB_USER = "airflow"
DB_PASS = "airflow"

def get_data(table_name):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"SELECT * FROM {table_name};")
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error connecting to DB: {e}")
        return pd.DataFrame()

# --- Load Data based on Queue Type ---
if queue_type == "M/M/1":
    df = get_data("mm1_results")
elif queue_type == "M/M/1/K":
    df = get_data("mm1k_results")

if df.empty:
    st.warning("No data available yet. Run simulations via Airflow DAGs.")
else:
    st.subheader("Simulation Data")
    st.dataframe(df)

    # --- Plot Example Metrics ---
    if queue_type == "M/M/1":
        fig, ax = plt.subplots()
        ax.plot(df["rho"], df["sim_L"], marker='o', label="Simulated L")
        ax.plot(df["rho"], df["theory_L"], marker='x', linestyle="--", label="Theoretical L")
        ax.set_xlabel("Rho (ρ)")
        ax.set_ylabel("Average Number in System (L)")
        ax.set_title("M/M/1: L vs Rho")
        ax.legend()
        st.pyplot(fig)

        fig2, ax2 = plt.subplots()
        ax2.plot(df["rho"], df["sim_W"], marker='o', label="Simulated W")
        ax2.plot(df["rho"], df["theory_W"], marker='x', linestyle="--", label="Theoretical W")
        ax2.set_xlabel("Rho (ρ)")
        ax2.set_ylabel("Average Time in System (W)")
        ax2.set_title("M/M/1: W vs Rho")
        ax2.legend()
        st.pyplot(fig2)

    elif queue_type == "M/M/1/K":
        fig, ax = plt.subplots()
        ax.plot(df["K"], df["sim_P_loss"], marker='o', label="Simulated P_loss")
        ax.plot(df["K"], df["theory_P_loss"], marker='x', linestyle="--", label="Theoretical P_loss")
        ax.set_xlabel("Queue Capacity (K)")
        ax.set_ylabel("Probability of Loss (P_loss)")
        ax.set_title("M/M/1/K: P_loss vs K")
        ax.legend()
        st.pyplot(fig)

        fig2, ax2 = plt.subplots()
        ax2.plot(df["K"], df["sim_L"], marker='o', label="Simulated L")
        ax2.plot(df["K"], df["theory_L"], marker='x', linestyle="--", label="Theoretical L")
        ax2.set_xlabel("Queue Capacity (K)")
        ax2.set_ylabel("Average Number in System (L)")
        ax2.set_title("M/M/1/K: L vs K")
        ax2.legend()
        st.pyplot(fig2)
