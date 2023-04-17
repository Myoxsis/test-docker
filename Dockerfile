FROM python:3.7.3-slim
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80

ENV NOM TESTDOCKER

CMD ["python", "main.py"]