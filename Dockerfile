FROM python:3.11.4-alpine3.18

RUN apk --no-cache -U upgrade && ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot/ bot/
CMD ["python", "-m", "bot"]
