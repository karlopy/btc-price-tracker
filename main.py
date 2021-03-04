import time, requests, datetime
from datetime import date
today = date.today()
d2 = today.strftime('%B %d, %Y')
print('BTC Price Tracker')
print('Made by: karlo#0001') #creds :D
print(d2)
yes = True
while yes == True: #loooooop
    data = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    json_data = data.json()
    price = json_data['USD'] #gets USD from the api
    time.sleep(90) #interval between each check, change number (seconds)
    print(price)
