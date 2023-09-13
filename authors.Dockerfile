FROM python:3.11.1-slim

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY authors-main.py /app
COPY library.json /app
EXPOSE 8000
ENV PYTHONPATH=/app
CMD ["uvicorn", "authors-main:app", "--host", "0.0.0.0", "--port", "8000"]
