FROM python:3.8-slim-buster
RUN apt-get update
RUN apt-get install -y python
ADD main.py /home/main.py
ADD main2.py /home/main2.py
ENTRYPOINT ["python"]
