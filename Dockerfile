FROM python:3.8-bullseye

WORKDIR /app

RUN pip install requests

COPY send_generate.py .

CMD [ "python", "send_generate.py" ]