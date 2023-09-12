FROM python:3.11.1-slim

WORKDIR /app

# install dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY books-main.py /app
COPY library.json /app
CMD ["uvicorn", "books-main:app", "--port", "7000", "--reload"]
