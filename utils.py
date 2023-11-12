import requests
import json
from config import currency

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException('Заданы одинаковые валюты!')

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConvertionException('Задана незнакомая валюта!')

        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConvertionException('Задана незнакомая валюта!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException('Ну удалось обработать такое колличество!')

        r = requests.get(f'https://api.coinbase.com/v2/exchange-rates?currency={quote_ticker}')
        total_base = float(json.loads(r.content)['data']['rates'][base_ticker])


        #r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        return total_base * amount
