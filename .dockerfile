# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV TWILIO_ACCOUNT_SID="dummy_sid_for_build"
ENV TWILIO_AUTH_TOKEN="dummy_token_for_build"
ENV TWILIO_PHONE_NUMBER="dummy_phone_for_build"

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Create necessary directories with proper permissions
RUN mkdir -p /app/static /app/staticfiles && chmod -R 755 /app/static /app/staticfiles

# Run Django management commands
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate 

# Expose port and run gunicorn
EXPOSE 8000
CMD ["gunicorn", "whatsapp_project.wsgi:application", "--bind", "0.0.0.0:8000"]