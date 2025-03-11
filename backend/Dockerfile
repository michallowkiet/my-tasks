FROM python:3.13-slim
# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

# Set the working directory to /app
WORKDIR /app

# # Copy the project into image
COPY . .

# Sync the project into new environment, using the frozen lockfile
RUN uv sync --frozen

# Expose port 8000 to communicate with the host
EXPOSE 8000

# Presuming there is a `my_app` command provided by the project
CMD ["uv", "run", "manage.py", "runserver","0.0.0.0:8000"]

# RUN chmod +x /app/entrypoint.sh 
# CMD ["/app/entrypoint.sh"]