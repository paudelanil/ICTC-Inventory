# Use an official Python runtime as the base image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE labinventory.settings

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/
RUN python manage.py makemigrations
# Run database migrations
RUN python manage.py migrate

# Load data from CSV file (adjust the path accordingly)
COPY data.csv /app/
RUN python manage.py insert_fromCSV

# Create a superuser (replace with your desired superuser credentials)
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

# Expose the port that the app runs on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
