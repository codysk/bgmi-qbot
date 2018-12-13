FROM python:3.6
WORKDIR /home/bgmi-qbot

COPY . .
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Shanghai

RUN { \
    pip install -r requirements.txt; \
}

CMD ["python", "run.py"]
