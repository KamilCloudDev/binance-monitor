import os
import time
from binance.client import Client
import requests
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

# Binance API credentials from environment variables
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Discord Webhook URL from environment variables
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Symbol to monitor
SYMBOL = "BTCPLN"

def send_discord_message(message):
    """Sends a message to a Discord channel via a webhook."""
    if not DISCORD_WEBHOOK_URL:
        print("Discord Webhook URL not found. Skipping notification.")
        return
    
    payload = {"content": message}
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Discord notification sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Discord notification: {e}")

def main():
    """Monitors Binance trades and sends Discord notifications."""
    if not API_KEY or not API_SECRET:
        print("Binance API credentials not set. Have you created a .env file?")
        return

    client = Client(API_KEY, API_SECRET)
    last_trade_id = None
    print(f"Starting to monitor trades for {SYMBOL}...")

    while True:
        try:
            trades = client.get_my_trades(symbol=SYMBOL, limit=1)
            if trades:
                current_trade = trades[0]
                current_trade_id = current_trade['id']

                print(f"Current last trade ID: {current_trade_id}")

                if last_trade_id is None:
                    # First run, send the most recent trade immediately
                    last_trade_id = current_trade_id
                    print(f"Initial trade ID set to: {last_trade_id}. Sending startup notification.")
                    
                    side = "KUPNO" if current_trade['isBuyer'] else "SPRZEDAŻ"
                    message = f"✅ MONITOR URUCHOMIONY. Ostatnia transakcja: {side} {current_trade['qty']} BTC @ {current_trade['price']} PLN"
                    
                    send_discord_message(message)

                elif current_trade_id != last_trade_id:
                    print(f"New trade detected! ID: {current_trade_id}")
                    last_trade_id = current_trade_id
                    
                    # Format the message for Discord
                    side = "KUPNO" if current_trade['isBuyer'] else "SPRZEDAŻ"
                    
                    message = f"🔔 NOWA TRANSAKCJA: {side} {current_trade['qty']} BTC @ {current_trade['price']} PLN"
                    
                    send_discord_message(message)
            else:
                print("No trades found yet.")

        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(60)

if __name__ == "__main__":
    main()
