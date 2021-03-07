## Creating a productised containerised Flask application

### Installation
Please ensure that you have Docker, Vagrant and Virtualbox already installed. This can 
be completed on Mac using the following command:

`brew install --cask docker vagrant virtualbox` 

**NB** There might occur an issue when installing Virtualbox for the first time using 
Brew. Virtualbox requires a kernel extension to operate, however, Apple requires user 
approval before loading a new third party kernel extension, therefore, you may need 
to give permission to allow this download. To enable the blocked kernel 
extension, navigate to `System Preferences > Security & Privacy > General`. Here, the 
message `System software from developer 'Oracle Corporation' was blocked from loading` 
will appear, click allow and retry downloading Virtualbox using Brew. 

### Introduction
The aim of this repository is to create a simple dockerized Flask web application. This 
application will be able to extract data contained in the body of a received POST 
request and will simply return the sum of these numbers. Finally, a Docker container 
will be deployed in a virtual machine with the aim of reproducing a production like 
environment. The virtual machine will be build and deployed using Vagrant and VirtualBox.    

### Flask Application
Flask is a WSGI web framework which is written in Python. It is lightweight and aims to 
facilitate an easy-to-extend philosophy. This means Flask provides you with tools, 
libraries and technologies that allow you to build a web application. This web 
application can be some web pages, a blog, a wiki or go as big as a web-based calendar 
application or a commercial website. It is designed to make getting started quick and 
easy, with the ability to scale up to complex applications.

The Flask application in this example is a very simple one. It ingests a POST request, 
converts the body of the POST request from a JSON object to a Python object. Next, it 
extracts and sums the values contained in the Python list object. Finally, the sum of 
the identified values is returned. 

To run the Flask application locally use the following command:
`python app/app.py`

Now that the Flask application is up and running you can use the following curl command 
to POST some data to the Flask application. The Flask application should be visible via 
port 5000 on the host network of your local machine (i.e. localhost). 
`curl -X POST -d '{"data": ["1", "2"]}' http://localhost:5000`

### Docker

Docker is an open platform for developing, shipping, and running applications. 
Docker enables you to separate your applications from your infrastructure so you can 
deliver software quickly. With Docker, you can manage your infrastructure in the 
same ways you manage your applications. Docker enables developers to easily pack, 
ship, and run any application as a lightweight, portable, self-sufficient container, 
which can run virtually anywhere. 

First you will need to create a Dockerfile. A Dockerfile contains the commands which 
allow the user to create their very own Docker image. Usually, this image is simply 
built upon another base image, which in this case is the Docker base python:3.7 image.
We also copy the Flask application mentioned above from our local machine into the 
Docker image.    

Once the Dockerfile has been created it is now possible to build a Docker image and 
create a Docker container running the Flask application. Docker build simply executes 
sequentially the commands contained in the Dockerfile to create a Docker image. To build 
the Docker image of the name `flask_app:latest`, use the following command:
`docker build . -t "flask_app:latest"`

Once the docker image has finished building (which may take some time), it is possible 
to create and run a Docker container. To create a Docker container based on the Docker 
image mentioned above use the following command:
`docker run -d -p 5000:5000 flask_app:latest`
The above command connects port 5000 of the local machine with port 5000 of the Docker 
container, therefore, allowing commands to be passed to the container via port 5000.

Now that the Docker container is up and running it is possible to post some data to it 
and see what it returns. To execute the Flask application through the Docker container 
use the following command: 
`curl -X POST -d '{"data": ["1", "2"]}' http://localhost:5000`

### Vagrant

Vagrant is a tool for building and managing a virtual machine environment in a single 
workflow. It is particularly useful when creating lightweight, reproducible and 
portable development environments. It makes the "works on my machine" excuse a relic of 
the past. It is very easy to simply spin up and run a virtual machine.

Similar to Docker, Vagrant uses a Vagrantfile to define a sequential list of commands
which when executed create a personalised virtual machine. Like Docker, Vagrant speeds 
up the building of a virtual machine by using a base image on which you can build a 
personalised virtual machine. These base images are called boxes. Virtual machines are 
really convenient for developing in and allow automatic syncs of files to and from the 
local machine. This way you can edit files locally and run them in your virtual machine 
development environment. By default, Vagrant shares your project directory (the one 
containing the Vagrantfile) to the `/vagrant` directory in your virtual machine.

Within the Vagrantfile the The Vagrant Docker provisioner has been defined. This 
automatically installs Docker, builds the docker image (as defined in the Dockerfile), 
and configures the Flask application container to run on boot of the virtual machine. 

To build the virtual machine using the following command (this may take a few minutes):
`vagrant up`

One can post data to the Docker container running within the virtual machine using the 
following command:
`curl -X POST -d '{"data": ["1", "2"]}' http://127.0.0.1:5000`
The virtual machine is defined to only be accessible via port 5000 of the IP `127.0.0.1`. 
Therefore, to pass the POST request to the Flask application the POST request is passed 
to port 5000 of the local machine which forwards the request to port 5000 of the virtual 
machine. Within the docker provisioning another forward port mapping was defined with port 
5000 of the virtual machine also mapped to port 5000 of the Docker container. As before,
the Docker container and the Flask application are also connected via their respective 
port 5000. Therefore, passing a POST request to port 5000 of your local machine will 
forward the request directly to the Flask application running within the virtual machine. 

### Conclusion
This repository contains all the details required to create your very own dockerized 
Flask application which is deployed within a production/development like environment.
This whole process has been extremely simplified, however, it provides a great example 
of how easy it is to create your very own web application running in your very own 
development environment.       