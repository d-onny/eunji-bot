FROM python:3.8.10-alpine3.12


RUN mkdir -p /project/tmp

WORKDIR /project
COPY requirements.txt bot.config src assets ./
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "src/start.py" ]