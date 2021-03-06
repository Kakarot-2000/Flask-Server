FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME OpentoAll

CMD ["python","app.py"]