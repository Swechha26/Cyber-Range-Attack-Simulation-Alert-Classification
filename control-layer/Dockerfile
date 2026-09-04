FROM python:3.10-slim

WORKDIR /app

COPY app.py /app/

RUN pip install flask requests

EXPOSE 5000

CMD ["python3", "app.py"]
