FROM python:3.6-slim

WORKDIR /code_etl

COPY requirements.txt /code_etl
RUN pip install -r requirements.txt
#ADD . /etl

CMD ["python", "etl.py"]
