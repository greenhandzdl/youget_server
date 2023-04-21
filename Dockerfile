FROM python:3.9-alpine

WORKDIR .
COPY . .

COPY requirements.txt .
RUN pip install -r requirements.txt



CMD ["python", "app.py"]