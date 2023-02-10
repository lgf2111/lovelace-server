# init a base image (python 3.11)
FROM python:3.11.1

# update pip
RUN pip install --upgrade pip

# define the working directory
WORKDIR /app

# copy contents of the server directory to the working directory
COPY . /app

# run pip install
RUN pip install -r requirements.txt

# determine if the server is running in docker
ARG IN_DOCKER=1

# gunicorn --certfile=ec2-cert.pem --keyfile=ec2-key.pem -b 0.0.0.0:443 run:app
CMD ["gunicorn", "--certfile=ec2-cert.pem", "--keyfile=ec2-key.pem", "-b", "0.0.0.0:80", "run:app"]
