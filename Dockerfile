FROM python:3.11

WORKDIR /wb-scraper

COPY requirements.txt /wb-scraper
RUN pip install --no-cache-dir -r requirements.txt

COPY . /wb-scraper

CMD ["python", "main.py"]
