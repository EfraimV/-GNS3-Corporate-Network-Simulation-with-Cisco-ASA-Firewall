FROM python:3.10-slim

RUN apt update && apt install -y iputils-ping

COPY ping_sweep.py /ping_sweep.py

CMD ["python", "/ping_sweep.py"]
