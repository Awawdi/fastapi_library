FROM python:3.11.1-slim

WORKDIR /app

# install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install fastapi uvicorn

COPY ./app /library_fastapi/app
CMD ["uvicorn", "app.main:app", "--reload", "--port", "5000"]