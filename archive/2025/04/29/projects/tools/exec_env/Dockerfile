# Dockerfile for Execution Environment

# Use a minimal, secure base image
FROM python:3.10-slim

WORKDIR /app

# Copy necessary files (tool logic, requirements)
# IMPORTANT: Ensure file_io.py is available at the specified relative path during build
# or adjust the COPY source path.
COPY ./file_io.py ./file_io.py
COPY ./exec_env/requirements.txt ./
COPY ./exec_env/main.py ./
# Copy config schema if needed by main.py for validation
# COPY ./config/allow_list.schema.yaml ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user for security
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser/app
# Re-copy files owned by appuser (adjust if needed based on base image WORKDIR)
COPY --chown=appuser:appuser ./file_io.py ./file_io.py
COPY --chown=appuser:appuser ./exec_env/requirements.txt ./
COPY --chown=appuser:appuser ./exec_env/main.py ./
# COPY --chown=appuser:appuser ./config/allow_list.schema.yaml ./

# TODO: Define how configuration (allow_list.yaml) is mounted at runtime
# Example: Expect config at /etc/fileio/allow_list.yaml

# Command to run the environment (e.g., start a listener)
CMD ["python", "main.py"] 