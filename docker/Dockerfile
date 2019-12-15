FROM python:3.6.9-slim

WORKDIR /app
COPY ./app/requirements.txt /app/requirements.txt

RUN apt-get install libglib2.0-0

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
