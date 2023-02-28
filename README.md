# Documenation of Whole Task

# Here's a general outline of the steps that I follow to complete the task:

1:I Choosed your Python to create my application.

2: Dockerize application by creating a Dockerfile. That enabled me to build an image that i can deploy in my container orchestration platform.

3: Set up a Git repository (GitHub) for my code and Dockerfile.

4: Choosed ( Github actions/workflow ) CI/CD tool to set up a pipeline to push and deploy the Docker image on EKS.

5: Choose ECS  to run your application.

6: Tested my application to ensure it is working as expected.

# Application
I have made a simple python application that includes the index.html, about.html, contact.html, and thanks.html pages along with the main app.py file and having requirments file as well.

# Docker file 

I also made a Dockerfile to build a Docker image that runs a Flask application on port 3000 and here is the working of Dockerfiel:

The Dockerfile first starts with the official Python 3.8.10 Docker image as the base image. 
Then it sets the working directory to /app, copies the requirements.txt file into the container, and installs the required Python packages with pip. 
After that, it copies the entire local directory (including the Flask app files) into the container.
Next, it exposes port 3000 to the host machine.
And finally, it sets the command to run when the container starts, which is to run python app.py.

# GitHub workflow for CI/CD
