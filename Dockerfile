FROM python:3.8.10

WORKDIR /app

COPY requirements.txt .
RUN pip install flask

COPY . .

EXPOSE 3000

CMD ["python", "app.py"]
