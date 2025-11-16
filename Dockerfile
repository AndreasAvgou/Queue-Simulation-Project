# General-purpose Dockerfile, defaulting to Python 3.11 slim
ARG BASE_IMAGE=python:3.11-slim
FROM ${BASE_IMAGE}

LABEL maintainer="yourname@example.com"
LABEL description="General-purpose Dockerfile for Python apps or Airflow/Streamlit"

# Switch to a non-root user
RUN useradd -m appuser
USER appuser
WORKDIR /home/appuser/app

# Copy and install Python dependencies if requirements.txt exists
COPY --chown=appuser:appuser requirements.txt ./
RUN if [ -f requirements.txt ]; then pip install --user --no-cache-dir -r requirements.txt; fi

# Copy all application code
COPY --chown=appuser:appuser . .

# Copy entrypoint script if it exists
COPY --chown=appuser:appuser entrypoint.sh /home/appuser/entrypoint.sh
RUN if [ -f /home/appuser/entrypoint.sh ]; then chmod +x /home/appuser/entrypoint.sh; fi

# Expose default ports
EXPOSE 8501 8080

# Flexible entrypoint and default command
ENTRYPOINT ["/home/appuser/entrypoint.sh"]
CMD ["streamlit", "run", "app_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
