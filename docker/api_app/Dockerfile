FROM python:3.6.9-slim

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
EXPOSE 5500

ENTRYPOINT ["python", "run.py"]
