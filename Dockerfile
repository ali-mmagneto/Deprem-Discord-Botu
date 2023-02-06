FROM ubuntu:20.04


RUN mkdir /app
RUN chmod 777 /app
WORKDIR /app


ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3","bot.py"]
