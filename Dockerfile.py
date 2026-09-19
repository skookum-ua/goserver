FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends python3
rm -rf /var/lib/apt/lists/*
EOF
CMD ["python3", "main.py"]