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
        "🚨 COMET ORANGE IS BACK IN STOCK!\n\n"
        "Size: UK 8\n"
        "👉 https://www.wearcomet.com/products/orange\n\n"
        "Go go go! 🏃"
    )
    print("In stock! Alert sent!")
else:
    print("Still sold out.")
```

4. Scroll down → click **"Commit changes"** → click **"Commit changes"** again

---

**PART 3 — Create the automation file**

This is the file that tells GitHub *when* to run your script automatically.

1. Click the **"+"** icon or **"Add file"** → **"Create new file"**
2. In the filename box, type **exactly** this (the slashes create folders automatically):
```
.github/workflows/check.yml
