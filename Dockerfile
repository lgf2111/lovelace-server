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

# define the command to run the server
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:3000"]