FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8080

COPY ./ /app

CMD ["python", "main.py"]