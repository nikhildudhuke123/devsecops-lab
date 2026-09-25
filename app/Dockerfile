FROM python:3.14-alpine AS builder

WORKDIR /build

COPY requirements.txt .
COPY init_db.py .

RUN apk update \
    && apk upgrade --no-cache
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
RUN python init_db.py


FROM python:3.14-alpine
RUN apk update && apk upgrade --no-cache

RUN addgroup -S -g 10001 appgroup && adduser -S -u 10001 -G appgroup appuser
WORKDIR /app
RUN chown -R appuser:appgroup /app

COPY --from=builder /install /usr/local
COPY --from=builder /build/users.db /app/users.db
RUN python -m pip uninstall -y pip

COPY app.py .

EXPOSE 5000

USER appuser
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
