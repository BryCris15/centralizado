FROM python:3.10-slim

WORKDIR /app

COPY app/ /app

RUN pip install fastapi uvicorn jinja2 httpx python-multipart

EXPOSE 3009

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3009"]