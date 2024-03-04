FROM python:3.11

WORKDIR /test

COPY requirements.txt /test
RUN pip install --no-cache-dir -r requirements.txt

COPY . /test

CMD ["python", "main.py"]
