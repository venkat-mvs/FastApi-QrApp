FROM python:3.9

WORKDIR /code

COPY ./requirments.py.txt /code/requirments.py.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirments.py.txt

COPY . /code/

WORKDIR /code/API

CMD [ "python", "main.py" ]