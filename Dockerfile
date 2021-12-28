FROM python:3.6

WORKDIR /app

RUN apt install git -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python", "-u", "main.py" ]
