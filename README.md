![Banner](banner.jpg)

[English](#-english-version) | [Polski](#-wersja-polska)

---

## 🇬🇧 English version

# Binance Trade Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple yet effective trade monitor for the Binance exchange, which sends notifications about new trades to a selected Discord channel via a webhook. The script is ready to be run in a Docker container.

---

## 🚀 Features

- **Trade Monitoring**: Tracks the latest trades for a specific currency pair (default: `BTCPLN`).
- **Discord Notifications**: Sends instant notifications about new trades.
- **Flexible Configuration**: All key data (API keys, webhook URL) are managed through environment variables.
- **Docker Ready**: Includes a `Dockerfile` for easy building and running in an isolated environment.
- **Local Testing**: Support for a `.env` file via `python-dotenv` makes local execution easy.

## 📋 Prerequisites

- Python 3.10+
- Docker (recommended for running)
- A Binance account with generated API keys.
- A Discord server with permissions to create webhooks.

## 🛠️ Setup and Configuration

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MrDead1987/binance-monitor.git
    cd binance-monitor
    ```

2.  **Configure environment variables:**
    Create a `.env` file in the project's root directory by copying or renaming the `.env.example` file (if it exists) or creating it from scratch. Fill it with your data:
    ```ini
    # Binance API Credentials
    BINANCE_API_KEY="YOUR_BINANCE_API_KEY"
    BINANCE_API_SECRET="YOUR_BINANCE_API_SECRET"

    # Discord Webhook URL
    DISCORD_WEBHOOK_URL="YOUR_DISCORD_WEBHOOK_URL"
    ```

3.  **Install dependencies (for local execution):**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Usage

### 1. Local Execution

Make sure you have correctly configured the `.env` file.
```bash
python monitor.py
```

### 2. Running with Docker (Recommended)

**a) Build the Docker image:**
```bash
docker build -t binance-monitor .
```

**b) Run the container, passing the environment variables:**
Replace the `your_...` values with your data.
```bash
docker run --name binance-monitor-app --rm \
  -e BINANCE_API_KEY="your_binance_api_key" \
  -e BINANCE_API_SECRET="your_binance_api_secret" \
  -e DISCORD_WEBHOOK_URL="your_discord_webhook_url" \
  binance-monitor
```
You can also use the `--env-file ./.env` option to load variables directly from the `.env` file:
```bash
docker run --name binance-monitor-app --rm --env-file ./.env binance-monitor
```

---


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
---

## 🇵🇱 Wersja polska

# Binance Trade Monitor

Prosty, ale skuteczny monitor transakcji na giełdzie Binance, który wysyła powiadomienia o nowych transakcjach na wybrany kanał Discord za pomocą webhooka. Skrypt jest gotowy do uruchomienia w kontenerze Docker.

---

## 🚀 Funkcjonalności

- **Monitorowanie transakcji**: Śledzi ostatnie transakcje dla określonej pary walutowej (domyślnie `BTCPLN`).
- **Powiadomienia na Discord**: Wysyła natychmiastowe powiadomienia o nowych transakcjach.
- **Elastyczna konfiguracja**: Wszystkie kluczowe dane (klucze API, URL webhooka) są zarządzane przez zmienne środowiskowe.
- **Gotowy na Docker**: Zawiera `Dockerfile` do łatwego budowania i uruchamiania w izolowanym środowisku.
- **Lokalne testowanie**: Wsparcie dla pliku `.env` dzięki `python-dotenv` ułatwia uruchamianie lokalne.

## 📋 Wymagania

- Python 3.10+
- Docker (zalecany do uruchomienia)
- Konto na giełdzie Binance z wygenerowanymi kluczami API.
- Serwer Discord z uprawnieniami do tworzenia webhooków.

## 🛠️ Instalacja i Konfiguracja

1.  **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/MrDead1987/binance-monitor.git
    cd binance-monitor
    ```

2.  **Skonfiguruj zmienne środowiskowe:**
    Stwórz plik `.env` w głównym katalogu projektu, kopiując lub zmieniając nazwę pliku `.env.example` (jeśli istnieje) lub tworząc go od zera. Wypełnij go swoimi danymi:
    ```ini
    # Binance API Credentials
    BINANCE_API_KEY="TWOJ_KLUCZ_API_BINANCE"
    BINANCE_API_SECRET="TWOJ_SEKRET_API_BINANCE"

    # Discord Webhook URL
    DISCORD_WEBHOOK_URL="TWOJ_DISCORD_WEBHOOK_URL"
    ```

3.  **Zainstaluj zależności (dla uruchomienia lokalnego):**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Użytkowanie

### 1. Uruchomienie lokalne

Upewnij się, że masz poprawnie skonfigurowany plik `.env`.
```bash
python monitor.py
```

### 2. Uruchomienie za pomocą Docker (zalecane)

**a) Zbuduj obraz Docker:**
```bash
docker build -t binance-monitor .
```

**b) Uruchom kontener z przekazaniem zmiennych środowiskowych:**
Zastąp wartości `your_...` swoimi danymi lub, jeśli używasz shella wspierającego `source`, wczytaj je z pliku `.env`.
```bash
docker run --name binance-monitor-app --rm \
  -e BINANCE_API_KEY="your_binance_api_key" \
  -e BINANCE_API_SECRET="your_binance_api_secret" \
  -e DISCORD_WEBHOOK_URL="your_discord_webhook_url" \
  binance-monitor
```
Możesz również użyć opcji `--env-file ./.env`, aby wczytać zmienne bezpośrednio z pliku `.env`:
```bash
docker run --name binance-monitor-app --rm --env-file ./.env binance-monitor
```

---


## 📄 Licencja

Projekt jest udostępniany na licencji MIT. Zobacz plik [LICENSE](LICENSE) po więcej szczegółów.

---
---

## 🇵🇱 Wersja polska