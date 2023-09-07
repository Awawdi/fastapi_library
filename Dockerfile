FROM python:3.11.1-slim

WORKDIR /app

# install dependencies
RUN pip freeze > requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /library_fastapi/app
CMD ["uvicorn", "app.main:app", "--reload", "--port", "5000"]