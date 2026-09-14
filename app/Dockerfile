FROM python:3.14-alpine AS builder

WORKDIR /build

COPY requirements.txt .

RUN apk update \
    && apk upgrade --no-cache
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.14-alpine
RUN apk update && apk upgrade --no-cache

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /app

COPY --from=builder /install /usr/local
RUN python -m pip uninstall -y pip

COPY app.py .

EXPOSE 5000

USER appuser
CMD ["python", "app.py"]
