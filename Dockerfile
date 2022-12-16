FROM python:3.8-slim-buster
RUN apt-get update
RUN apt-get install -y python
ADD main.py /home/hello.py
CMD ["/home/hello.py"]
ENTRYPOINT ["python"]
