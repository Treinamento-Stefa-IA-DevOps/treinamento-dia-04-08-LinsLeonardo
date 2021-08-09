FROM python:3.8-slim

COPY . /codigo

WORKDIR /codigo

RUN pip install --upgrade pip

RUN pip install fastapi[all]

RUN pip install pandas sklearn 

CMD ["uvicorn", "codigo.main:app","--host", "0.0.0.0", "--port", "8080", "--reload"]
