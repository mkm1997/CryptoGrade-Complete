from django.core.management.base import BaseCommand
from CoinViewer.models import Coin, TotalRating


class Command(BaseCommand):
    help = "manually retallies all totals for all coins"

    def handle(self, *args, **options):
        for coin in Coin.objects.all():
            for tr in TotalRating.objects.filter(coin=coin):
                tr.retally()
                tr.save()
            coin.retally()
            coin.save()
