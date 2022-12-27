FROM python:3.8

WORKDIR /app
# copear dependencias, izquierda=archivo local, derecha= nuevo
COPY requirements.txt  /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r  /app/requirements.txt 

# . significa que hay que copear todo lo de ese directorio
COPY . / app/

CMD bash -c "while true; do sleep 1; done"