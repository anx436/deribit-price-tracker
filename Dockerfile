FROM python:3.10-slim-trixie

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make the startup script executable
RUN chmod +x start.sh

EXPOSE 8000

# This runs our start.sh when the container starts
CMD ["./start.sh"]
