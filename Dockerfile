FROM python:3.12-slim

WORKDIR /app

COPY . /app

EXPOSE 9267

CMD ["python", "flask_app.py"]