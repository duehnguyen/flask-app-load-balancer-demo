FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV ECS_CLUSTER=\
  ECS_SERVICE=\
  CONTAINER_NAME=

EXPOSE 8081 

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

