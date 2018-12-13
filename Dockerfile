FROM python:3.6
WORKDIR /home/bgmi-qbot

COPY . .
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Shanghai
ENV DATA_PATH /data

VOLUME ['/data']

RUN { \
    pip install -r requirements.txt; \
}

CMD ["python", "run.py"]
