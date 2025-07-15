FROM python:3.13-slim

WORKDIR /app
# this to link container to repository
#LABEL org.opencontainers.image.source=https://github.com/vadym11/devopsproject2025

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]