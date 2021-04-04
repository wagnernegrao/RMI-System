FROM python:3.8.9-buster

RUN pip install --upgrade pip
RUN pip install Pyro4
RUN pip install pandas
