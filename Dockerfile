FROM python:3.12-alpine
WORKDIR /app
COPY app/ ./app/
COPY config/ ./config/
RUN python -m compileall -q app && adduser -D -H appuser
USER appuser
EXPOSE 8080
CMD ["python", "-m", "app.main"]
