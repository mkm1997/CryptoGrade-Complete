from django.core.management.base import BaseCommand
from CoinViewer.models import Coin, RatingCategory, TotalRating
from django.utils import timezone
import json
import requests

coins_tracked = [
    'BTC',
    'ETH',
    'XRP',
    'BCH',
    'LTC',
    'ADA',
    'NEO',
    'XLM',
    'EOS',
    'MIOTA',
    'DASH',
    'XEM',
    'XMR',
    'LSK',
    'TRX',
    'ETC',
    'VEN',
    'QTUM',
    'BTG',
    'USDT',
    'ICX',
    'OMG',
    'ZEC',
    'XRB',
    'XVG',
    'BNB',
    'STEEM',
    'PPT',
    'BCN',
    'SC',
    'STRAT',
    'RHOC',
    'SNT',
    'DOGE',
    'WAVES',
    'BTS',
    'MKR',
    'WTC',
    'ZRX',
    'DCR',
    'AE',
    'UCASH',
    'REP',
    'VERI',
    'HSR',
    'KMD',
    'ZCL',
    'KCS',
    'ETN',
    'ARDR',
    'R',
    'ARK',
    'DGD',
    'DRGN',
    'GAS',
    'DGB',
    'BAT',
    'GBYTE',
    'LRC',
    'ZIL',
    'GNT',
    'BTM',
    'KNC',
    'MONA',
    'PIVX',
    'SYS',
    'ELF',
    'QASH',
    'CNX',
    'DCN',
    'AION',
    'BTX',
    'NAS',
    'IOST',
    'ETHOS',
]


class Command(BaseCommand):
    help = "pulls coin data from CMC api"

    def handle(self, *args, **options):
        url_usable = "https://api.coinmarketcap.com/v1/ticker/?start=0&limit=100"
        response = requests.get(url_usable)
        text = response.text
        data = json.loads(text)

        for coin in data:
            if coin['symbol'] in coins_tracked:

                # If the coin already is in the DB, we merely update the information
                if Coin.objects.filter(name=coin['name']).exists():
                    current = Coin.objects.filter(name=coin['name']).first()
                    current.name = coin['name']
                    current.cmc_id = coin['id']
                    current.ticker = coin['symbol']
                    current.price_usd = round(float(coin['price_usd']), 2)
                    current.market_cap = float(coin['market_cap_usd'])
                    current.rank = coin['rank']
                    current.info_updated_at = timezone.now()
                    current.save()

                # If the coin isn't yet tracked, we must enter it into the DB and create ratings for it
                else:

                    # First create the coin object
                    coinobj = Coin.objects.create(
                        name=coin['name'],
                        cmc_id=coin['id'],
                        ticker=coin['symbol'],
                        price_usd=round(float(coin['price_usd']), 2),
                        market_cap=float(coin['market_cap_usd']),
                        total_rank=coin['rank']
                    )
                    coinobj.save()

                    # Next, create a TotalRating for each RatingCategory and FK it to the coin
                    for cat in RatingCategory.objects.all():
                        tr = TotalRating.objects.create(
                            category=cat,
                            coin=coinobj
                        )
                        tr.save()
