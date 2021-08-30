FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

RUN pip3 install psycopg2-binary && \
    pip3 install psycopg2

COPY ./requirements.txt ./
COPY ./requirements-dev.txt ./
RUN pip3 install -r ./requirements.txt
RUN pip3 install -r ./requirements-dev.txt

COPY docker-entrypoint.sh ./
RUN chmod u+x docker-entrypoint.sh

WORKDIR /emenu
VOLUME ["/emenu"]

EXPOSE 8000

CMD /docker-entrypoint.sh