import requests
from colorama import init, Fore

init(autoreset=True)

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,rub"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    btc_usd = data["bitcoin"]["usd"]
    btc_rub = data["bitcoin"]["rub"]

    print(f"Курс BTC/RUB: ₽{Fore.GREEN}{btc_rub}")
    print(f"Курс BTC/USD: ${Fore.GREEN}{btc_usd}")

else:
    print(Fore.RED + f"Ошибка загрузки данных. Код: {response.status_code}")