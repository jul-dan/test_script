FROM python:3.8-slim-buster
ADD main.py /home/main.py
ADD main2.py /home/main2.py
CMD ["/home/main.py"]
ENTRYPOINT ["python"]
