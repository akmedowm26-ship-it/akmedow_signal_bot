import time
import os
import requests

# Siziň Telegram Maglumatlaryňyz
TOKEN = "8871699370:AAFfUzQQvVCZKtqzGHCo2JUVuV9F-E9tEI8"
CHAT_ID = "7431522485"

# Yzarlanmaly 24 sany esasy jübütler (Forex, Altyn we Kripto)
PAIRS = [
    "XAUUSD", "BTCUSD", "EURUSD", "GBPUSD", "USDJPY", 
    "AUDUSD", "USDCAD", "NZDUSD", "USDCHF", "EURGBP", 
    "EURJPY", "GBPJPY", "AUDJPY", "EURAUD", "EURNZD", 
    "GBPAUD", "GBPCAD", "GBPNZD", "AUDCAD", "AUDNZD", 
    "NZDCAD", "CADJPY", "CHFJPY"
]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Ýalňyşlyk: {e}")

def check_indicators_and_trade():
    print("Bot 24 sany jübüt boýunça bazara gözegçilik edýär...")
    
    for pair in PAIRS:
        # Range Filter (B&S) we MSB-OB (Order Block) şertleri:
        # Diňe ikisi hem birlikde BUY ýa-da SELL berende True bolýar.
        buy_condition_met = False   
        sell_condition_met = False  
        current_price = "4030.00"   # Hakyky baha ýa-da API bahasy
        
        # 1-nji Wariant (Modern / Premium format)
        if buy_condition_met:
            msg = f"💎 **{pair}**\n━━━━━━━━━━━━━━━━━━\n🎯 **SIGNAL:** BUY\n⚡ **ENTRY:** {current_price}\n━━━━━━━━━━━━━━━━━━\n🚀 Status: Active"
            send_telegram_message(msg)
            
        if sell_condition_met:
            msg = f"💎 **{pair}**\n━━━━━━━━━━━━━━━━━━\n🎯 **SIGNAL:** SELL\n⚡ **ENTRY:** {current_price}\n━━━━━━━━━━━━━━━━━━\n🚀 Status: Active"
            send_telegram_message(msg)

if __name__ == "__main__":
    send_telegram_message("🤖 **Signal Bot üstünlikli işläp başlady!** 24 jübüt boýunça 7/24 gözegçilik edýär.")
    
    while True:
        try:
            check_indicators_and_trade()
        except Exception as e:
            print(f"Ýalňyşlyk: {e}")
        
        # Her 30 sekuntda bir bazary barlap durýar
        time.sleep(30)
      
