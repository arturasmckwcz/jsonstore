FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 3000

ENV FLASK_ENV=production

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
