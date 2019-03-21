from django.core.management.base import BaseCommand, CommandError
from CoinViewer.models import TotalRating, Coin


class Command(BaseCommand):
    help = "recalculates all totalratings"

    def handle(self, *args, **options):
        print("Recalculating all TotalRating scores... please be patient.")
        trs = TotalRating.objects.all()
        for tr in trs:
            tr.recalculate()
            tr.save()

        print("Recalculating all Coin scores... please be patient.")
        coins = Coin.objects.all()
        for coin in coins:
            coin.recalculate()
            coin.save()
