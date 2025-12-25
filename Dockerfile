# Use the official Python image.
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY monitor.py .

# Pass environment variables at runtime, e.g.:
# docker run -e BINANCE_API_KEY="key" -e BINANCE_API_SECRET="secret" -e DISCORD_WEBHOOK_URL="url" <image_name>

CMD ["python", "-u", "monitor.py"]
