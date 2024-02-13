FROM python:3.10

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local app directory to the working directory
COPY ./app /app

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
