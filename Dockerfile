FROM python:3.12-slim

ENV PATH="/opt/venv/bin:$PATH"
ENV GRADIO_SERVER_NAME="0.0.0.0"
EXPOSE 7860

WORKDIR /app

RUN apt update && \
    python3 -m venv /opt/venv

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

CMD . /opt/venv/bin/activate && \
    python3 main.py
