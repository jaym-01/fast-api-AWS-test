FROM python:3

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "src.main:app", "--port", "8080", "--host", "0.0.0.0"]