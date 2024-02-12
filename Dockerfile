
# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR / G:\ML Intern at Celloscope\Demo_01

# Copy the requirements file into the container at /app
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the current directory contents into the container at /app
COPY . .

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
