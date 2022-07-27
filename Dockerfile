# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
# update pip to minimize dependency errors
RUN pip install --upgrade pip
# define the present working directory
WORKDIR /Emaww
EXPOSE 5000
# copy the contents into the working dir
# run pip to install the dependencies of the flask app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# define the command to start the container
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]