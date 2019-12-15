FROM python:3.6.9-slim

WORKDIR /app
COPY ./api/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
