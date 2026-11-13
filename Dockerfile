# Multi-stage Dockerfile for Solana-Geyser-Stream-Detector
FROM python:3.11-slim as builder

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim as runner

WORKDIR /app
RUN groupadd -r geyser && useradd -r -g geyser geyser

COPY --from=builder /root/.local /home/geyser/.local
COPY --chown=geyser:geyser . /app

ENV PATH=/home/geyser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER geyser

ENTRYPOINT ["python", "cli.py"]
CMD ["demo"]
