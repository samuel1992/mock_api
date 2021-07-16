FROM python:3.8

EXPOSE 8000

RUN mkdir /mock-api
WORKDIR /mock-api

COPY requirements.txt /mock-api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /mock-api

CMD python /mock-api/manage.py migrate
CMD python /mock-api/manage.py runserver 0.0.0.0:8000
