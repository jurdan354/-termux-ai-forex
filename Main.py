import time
import random

# Simulasi AI Sinyal Forex
while True:
    harga = round(random.uniform(1900, 2000), 2)
    sinyal = random.choice(['BUY 💚', 'SELL ❤️'])
    print(f"[AI Sinyal XAUUSD] {sinyal} di harga {harga}")
    time.sleep(15 * 60)  # setiap 15 menit kirim sinyal baru
