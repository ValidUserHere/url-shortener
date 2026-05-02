FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn redis

EXPOSE 8000

CMD ["uvicorn", "url_sh:app", "--host", "0.0.0.0", "--port", "8000"]

