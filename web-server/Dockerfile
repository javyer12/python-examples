FROM python:3.10

WORKDIR /app
# copear dependencias, izquierda=archivo local, derecha= nuevo
COPY requirements.txt  /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r  /app/requirements.txt 

# . significa que hay que copear todo lo de ese directorio
COPY .  /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]