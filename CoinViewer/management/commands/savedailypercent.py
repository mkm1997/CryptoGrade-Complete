from django.core.management.base import BaseCommand
from CoinViewer.models import Coin
from django.utils import timezone
import json
import requests


class Command(BaseCommand):
    help = "pulls coin data from CMC api"

    def handle(self, *args, **options):
        for coin in Coin.objects.all():
            coin.save_daily_percent()
            coin.pct_change_color = "black"
            coin.save()
