FROM python:3.9

WORKDIR /main

COPY ./requirments.txt /main/requirments.txt

RUN pip install --no-cache-dir --upgrade -r /main/requirments.txt

COPY . /main/

WORKDIR /main/API

ENV HOST=0.0.0.0 \
    API_TITLE=QrApp \
    API_VERSION=0.1.1 \
    PORT=8000

CMD [ "python", "main.py" ]