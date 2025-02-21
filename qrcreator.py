import qrcode

ssid = "Depot 4G"
security = "WPA"  # Or "WPA2", "WEP" if applicable
password = "depot6688"
url = "http://192.168.29.45:8000/"

# Correct Wi-Fi QR code format:
wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

qr_data = wifi_config + "\n" + url # Combine wifi and url
qr = qrcode.make(qr_data)
qr.save("wifi_url_qr.png")

print(f"QR code saved to wifi_url_qr.png") # Confirmation message