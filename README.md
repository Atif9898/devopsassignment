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
I have made a GitHub Action that automates building and pushing a Docker image to Amazon ECR when code is pushed to the main branch. 
Here's a brief overview of what each step in the script does:

on section specifies the event that triggers the action, which in this case is a push to the main branch.
 env section sets environment variables that will be used throughout the script, such as the AWS region and the ECR repository name.
 jobs section defines the jobs that will be run as part of this action. In this case, there is only one job called build-and-push.
 runs-on section specifies the type of runner that will be used for the job. In this case, it is ubuntu-latest.
The steps section defines the steps that will be run as part of the job.
 Checkout code step checks out the repository code.
 Configure AWS credentials step sets up the AWS access credentials that will be used to authenticate with ECR.
The Login to Amazon ECR step logs in to the specified ECR registry using the AWS access credentials.
 Build and push Docker image to Amazon ECR step builds the Docker image using the Dockerfile in the repository, tags it with a unique identifier based on the commit SHA, and pushes it to ECR.
 
 # Github
 we are having our all code and dockerfile on Github along with the credenations for Aws stored as secrets in the setting under secrets and variables under actions in Repository secrets.
 named as AWS_ACCESS_KEY_ID   , AWS_SECRET_ACCESS_KEY


 
 
 ## Deployment 
 
 As we alreday have pushed our image on ECR so now we have to do follwing:
 Note: we are having 
 
 # Load balancer
 Here are the steps to make a load balancer 
 Go to the AWS Management Console and navigate to the EC2 dashboard.
Click on "Load Balancers" in the left-hand menu.
Click on "Create Load Balancer" and choose "Application Load Balancer".
Enter a name for your load balancer and choose the VPC and subnets that you want to use.
Configure the "Security Settings" and "Security Groups" as per your requirements.
On the "Configure Routing" page, create a new target group by clicking on "Create Target Group".
Give your target group a name, choose the target type as "IP", and configure the health check settings as per your requirements.
Choose the instances that will be part of your target group by selecting the appropriate values for "Target Group Name", "Protocol", "Port", and "Target type".
Click on "Next" and configure the "Load Balancer Protocol" and "Listener Configuration" as per your requirements.
Review your load balancer settings and click on "Create" to create the load balancer and target group.

 
