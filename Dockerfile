FROM python:3.10

ENV PYTHONUNBUFFERED=1 TIMEZONE=UTC+2
RUN apt-get update

RUN mkdir -p /usr/src/app/
ARG WORKDIR=/usr/src/app/

WORKDIR ${WORKDIR}

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install --requirement requirements.txt
COPY . /usr/src/app/

ARG USER=user
ARG UID=1000

RUN useradd --system ${USER} --uid=${UID}

RUN chown --recursive ${USER} ${WORKDIR}

EXPOSE 8000


VOLUME ${WORKDIR}/db
CMD python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py runserver 0.0.0.0:8000