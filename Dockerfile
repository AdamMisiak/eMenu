FROM python:3

ENV PYTHONUNBUFFERED=1

RUN pip3 install psycopg2-binary && \
    pip3 install psycopg2

WORKDIR /app

COPY ./requirements.txt ./
COPY ./requirements-dev.txt ./
RUN pip3 install -r ./requirements.txt
RUN pip3 install -r ./requirements-dev.txt

EXPOSE 8000

COPY ./emenu /app/
COPY docker-entrypoint.sh ./
RUN chmod u+x docker-entrypoint.sh

CMD ./docker-entrypoint.sh