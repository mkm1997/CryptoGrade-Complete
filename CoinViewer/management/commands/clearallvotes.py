from django.core.management.base import BaseCommand, CommandError
from CoinViewer.models import TotalRating, CoinRating, Coin
from builtins import input


class Command(BaseCommand):
    help = "clears all votes in the server"

    def handle(self, *args, **options):
        choice = input("Are you sure you wish to clear all votes? This is not reversible! Type YESSIRIDO to confirm: ")
        if choice == "YESSIRIDO":
            final_choice = input("Seriously? Think long and hard about this... type PUSHTHEBUTTON to do it: ")
            if final_choice == "PUSHTHEBUTTON":

                print("Deleting all vote records and data from the DB...")

                # Reset all totalratings to initial counts
                trs = TotalRating.objects.all()
                for tr in trs:
                    tr.votes_pro = 0
                    tr.votes_con = 0
                    tr.recalculate()
                    tr.save()

                # Reset coin totals to initial counts
                coins = Coin.objects.all()
                for coin in coins:
                    coin.total_votes_pro = 0
                    coin.total_votes_con = 0
                    coin.recalculate()
                    coin.save_daily_percent()
                    coin.recalculate()
                    coin.save()

                # Delete all CoinRatings
                CoinRating.objects.all().delete()

            else:
                print("Aborting...")
        else:
            print("Aborting...")
