import requests

TELEGRAM_TOKEN = "8204726896:AAH05oOcLQLnph652AWo3UtiMM3ZhXNMNek"
CHAT_ID = "763131291"
TARGET_COLOR = "Orange Cream"
TARGET_SIZE = "8"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def check_stock():
    try:
        response = requests.get("https://www.wearcomet.com/products/orange.json", timeout=10)
        data = response.json()
        for variant in data["product"]["variants"]:
            if TARGET_COLOR in variant["title"] and f"/ {TARGET_SIZE}" in variant["title"]:
                return variant["available"]
    except Exception as e:
        print(f"Error: {e}")
    return False

if check_stock():
    send_telegram(
        "✅ COMET ORANGE IS BACK IN STOCK!\n\n"
        "Size: UK 8\n"
        "Buy now: https://www.wearcomet.com/products/orange\n\n"
        "Go go go!"
    )
else:
    send_telegram(
        "❌ Comet Orange (UK 8) is still sold out.\n"
        "I'll check again and will let you know shortly!"
    )
