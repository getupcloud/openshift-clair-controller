FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY klar /

RUN pip install --no-cache-dir claircontroller

USER 1001

CMD [ "clair-controller" ]
