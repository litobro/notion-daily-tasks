# Choose a base image
FROM python:3.10

# Don't need .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Turn off buffer for container output
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
WORKDIR /app

# Add and run as non-root user
RUN adduser --disabled-password --gecos '' appuser  && chown -R appuser /app
USER appuser

# Run the command
CMD ["python", "main.py"]