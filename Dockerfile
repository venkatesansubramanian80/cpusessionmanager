FROM python:3.8

EXPOSE 8080

WORKDIR /app

COPY requirements.txt /app
COPY app.py /app

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y tmux

CMD python app.py