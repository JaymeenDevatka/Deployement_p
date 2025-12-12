# -------- Base Image --------
FROM python:3.11-slim

# -------- Work Directory --------
WORKDIR /app

# -------- Copy dependencies --------
COPY requirements.txt .

# Install pip first
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# -------- Copy project files --------
COPY . .

# -------- Expose port --------
EXPOSE 8000

# -------- Command to run Gunicorn --------
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app.main:create_app()"]
