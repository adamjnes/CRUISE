# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
RUN mkdir /cruise
WORKDIR /cruise
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# CMD ["python3", "src/launch.py"]
CMD python3 src/launch.py && bash