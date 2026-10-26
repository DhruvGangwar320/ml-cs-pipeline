# Pull the python image from Docker Hub
# Use a lightweight Python image to reduce the size of the final Docker image
FROM python:3.14-slim 
# lightweight image with python 3.14

# now all code of main.py into docker environment

# for that we need a folder with the code to be copied into the docker image
# set the working directory inside container
WORKDIR /app

COPY requirement.txt .
RUN pip install -r requirement.txt
# Copy the application code into the container and saved model inside /app directory
# First dot means the build context; second dot means the container's current directory
COPY . .
# Expose the port that the application will run on
EXPOSE 8000 

# "0.0.0.0" means that the apuplication will be accessible from outside the container , all IPs are allowed to access the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# run the application using uvicorn server