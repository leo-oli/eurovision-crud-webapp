# Use the Python 3.11 Alpine Linux image as the base image
FROM python:3.11-alpine

# Set the working directory to /app inside the container
WORKDIR /app

# Copy dump.sql to the /app directory in the container
COPY db/dump.sql db/

# Update all packages
RUN apk update && apk upgrade

# Install sqlite
RUN apk add --no-cache sqlite

# Import database
RUN echo ".read db/dump.sql" | sqlite3 db/eurovisiondb.sqlite

# Copy requirements.txt to the /app directory in the container
COPY requirements.txt .

# Install the required Python packages listed in the requirements.txt file
RUN pip install -r requirements.txt

# Copy the current directory to the /app directory in the container
COPY . .

# Expose port for external connections to the Flask app running inside the container
EXPOSE 5000

#  Set the command to run the Flask app when the container starts
CMD [ "python", "-m", "src.app" ]
