FROM python:3.12-alpine
#FROM alpine:3.21

WORKDIR /app

#COPY backend_test /usr/local/bin/backend
COPY backend.py /app/backend.py
#COPY data/ /data/

#RUN chmod +x /usr/local/bin/backend
RUN pip install --no-cache-dir flask

EXPOSE 3000

ENV BACKEND_PORT=3000

CMD ["python", "/app/backend.py"]
#ENTRYPOINT ["sh", "-c", "backend --port ${BACKEND_PORT} --data /data/provider-alpha.json,/data/provider-beta.json,/data/provider-gamma.json"]
