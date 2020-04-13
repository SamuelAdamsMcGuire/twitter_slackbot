FROM python:3.6-slim

WORKDIR /etl

COPY requirements.txt /etl
RUN pip install -r requirements.txt
ADD . /etl

CMD ["python", "etl.py"]
