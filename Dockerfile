FROM python:3.8-slim-buster
ADD job.py job.py
ADD cronjob.py cronjob.py
CMD ["cronjob.py"]
ENTRYPOINT ["python"]
