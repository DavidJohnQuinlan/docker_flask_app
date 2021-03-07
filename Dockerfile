# define the base image on which this image is based
# in this case the base image is the Python3.7 Docker image
FROM python:3.7

# define the maintainer
MAINTAINER David Quinlan

# add additional content to the image
# update the package information and install python and pip
RUN apt-get update -y && apt-get install -y python3-pip python3-dev

# copy a file/directory from the host machine to the container during the build process
COPY ./ /

# install the necessary requirements
RUN pip install -r requirements.txt

# use Python to execute the Flask application
CMD [ "python3", "app/app.py" ]