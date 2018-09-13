FROM python:2

WORKDIR /runner
RUN pip install pipenv
RUN pipenv install
