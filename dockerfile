FROM python:3.11-slim

# Prevent .pyc files
ENV PYTHONDONTWRITEBYTECODE 1  
# Enable stdout/stderr buffering
ENV PYTHONUNBUFFERED 1       

WORKDIR /Blog

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/production.txt /Blog/
RUN pip install --no-cache-dir -r production.txt

# Copy the project files
COPY . /Blog/

# Collect static files (for production)
RUN python manage.py collectstatic --noinput

# Expose port for Gunicorn
EXPOSE 8000

# Start Gunicorn server with specified settings
CMD ["gunicorn", "Blog.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
