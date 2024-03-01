FROM python:3.9-slim

RUN mkdir -p /app
RUN mkdir -p /app/data
RUN mkdir -p /app/data/model
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY config /app/config
COPY test /app/test
COPY models /app/models
COPY utils /app/utils
COPY app.py /app

EXPOSE 7860

CMD [ "python3", "/app/app.py" ]