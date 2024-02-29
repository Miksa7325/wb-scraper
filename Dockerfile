FROM python:3.11

WORKDIR /WildberriesProject

COPY requirements.txt /WildberriesProject
RUN pip install --no-cache-dir -r requirements.txt

COPY . /WildberriesProject

CMD ["python", "main.py"]
