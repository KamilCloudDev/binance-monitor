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
        print("Discord Webhook URL not found. Skipping notification.", flush=True)
        return
    
    payload = {"content": message}
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Discord notification sent successfully.", flush=True)
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Discord notification: {e}", flush=True)

def send_startup_notification():
    """Sends a notification that the bot has started."""
    print("Sending startup notification to Discord.", flush=True)
    send_discord_message("🤖 Bot monitorujący został uruchomiony.")

def main():
    """Monitors Binance trades and sends Discord notifications."""
    if not API_KEY or not API_SECRET:
        print("Binance API credentials not set. Have you created a .env file?", flush=True)
        return

    client = Client(API_KEY, API_SECRET)
    last_trade_id = None

    # Send startup notification before the main loop
    send_startup_notification()
    
    print(f"Starting to monitor trades for {SYMBOL}...", flush=True)

    while True:
        try:
            trades = client.get_my_trades(symbol=SYMBOL, limit=1)
            if trades:
                current_trade = trades[0]
                current_trade_id = current_trade['id']

                print(f"Current last trade ID: {current_trade_id}", flush=True)

                if last_trade_id is None:
                    # First run, send the most recent trade immediately
                    last_trade_id = current_trade_id
                    print(f"Initial trade ID set to: {last_trade_id}. Sending last known trade.", flush=True)

                    # --- Message Formatting ---
                    price_pln = float(current_trade['price'])
                    qty_btc = float(current_trade['qty'])
                    side = "KUPNO" if current_trade['isBuyer'] else "SPRZEDAŻ"
                    
                    formatted_pln = f"{price_pln:.2f}"
                    formatted_btc = f"{qty_btc:.8f}".rstrip('0').rstrip('.')
                    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_trade['time'] / 1000))

                    message = (
                        f"✅ **Ostatnia znana transakcja** ✅\n\n"
                        f"**Typ:** {side}\n"
                        f"**Ilość:** {formatted_btc} BTC\n"
                        f"**Cena:** {formatted_pln} PLN\n"
                        f"**Czas:** {formatted_time}"
                    )
                    
                    send_discord_message(message)

                elif current_trade_id != last_trade_id:
                    print(f"New trade detected! ID: {current_trade_id}", flush=True)
                    last_trade_id = current_trade_id
                    
                    # --- Message Formatting ---
                    price_pln = float(current_trade['price'])
                    qty_btc = float(current_trade['qty'])
                    side = "KUPNO" if current_trade['isBuyer'] else "SPRZEDAŻ"
                    
                    formatted_pln = f"{price_pln:.2f}"
                    formatted_btc = f"{qty_btc:.8f}".rstrip('0').rstrip('.')
                    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_trade['time'] / 1000))
                    
                    message = (
                        f"🔔 **NOWA TRANSAKCJA** 🔔\n\n"
                        f"**Typ:** {side}\n"
                        f"**Ilość:** {formatted_btc} BTC\n"
                        f"**Cena:** {formatted_pln} PLN\n"
                        f"**Czas:** {formatted_time}"
                    )
                    
                    send_discord_message(message)
            else:
                print("No trades found yet.", flush=True)

        except Exception as e:
            print(f"An error occurred: {e}", flush=True)

        time.sleep(60)

if __name__ == "__main__":
    main()
