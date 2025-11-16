FROM python: 3.11

WORKDIR /flask-hitelkalkulator

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "application.py"]
