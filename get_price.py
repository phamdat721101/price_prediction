import re
import sys
import time
import datetime
import requests
import json
import csv

def fetch_price():
    headers = {'X-API-VERSION': 'v1'}
    response_API = requests.get('https://fpticker-api.stg.vncdevs.com/api/candles?symbol=EURUSD&timeframe=M5&from_time=1701833651&to_time=1701844451', headers=headers)
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    print("Data information: ", parse_json['data'][0])
    
    with open('eur_usd_test.csv', mode='w') as csv_file:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for candle in parse_json['data']:
            writer.writerow({'Date': candle['datetime'], 'Open': candle['open'], 'High': candle['high'], 'Low': candle['low'], 'Close': candle['close']})

if __name__ == '__main__':
    fetch_price()