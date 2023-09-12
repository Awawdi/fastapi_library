FROM python:3.11.1-slim

WORKDIR /app

# install dependencies
COPY ./fastapi_library/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install fastapi uvicorn

COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
