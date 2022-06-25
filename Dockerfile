FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./digitaleasyproj /digitaleasyproj
COPY ./scripts /scripts


WORKDIR /digitaleasyproj
EXPOSE 8000

RUN python -m venv /py && \
    apk update && \
    apk add mariadb-dev linux-headers build-base && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts
##Se añade la version de python del entorno virtual al path \
ENV PATH="/scripts:/py/bin:$PATH"

##create user different from root

USER app
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
CMD ["run.sh"]