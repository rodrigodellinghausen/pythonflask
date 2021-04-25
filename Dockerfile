FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3.8 -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "./teste.py" ]