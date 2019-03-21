from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from CoinViewer.models import CoinRating, Coin, TotalRating
import random
import time
import math

class Command(BaseCommand):
    help = "uses voting algorithm to fabricate vote counts"

    def handle(self, *args, **options):

        # First get the AdminUser account and associated data
        adminuser = User.objects.get(username="Manish")
        coins = Coin.objects.all()
        num_coins = len(coins)




        print(num_coins)

        # Wait a random number of seconds to simulate realism
        '''sleeptime = random.randint(1, 59)
        time.sleep(sleeptime)
        print("hello world")'''

        # Get a randomly selected coin and its associated TotalRating objects
        coin = coins[random.randint(0, num_coins-1)]
        categories = TotalRating.objects.filter(coin=coin)
        #print(categories)
        #############################################################
        #i will use it later
        cats = TotalRating.objects.filter(coin=coin)
        #cats = cats.order_by('priority')

        ################### Fake vote Loop ###################

        #percent_inc_list = random.sample(range(40, 75), 71)

########################################### Main Updating Code ##################################################
        for coin in coins[:10]:
            cats = TotalRating.objects.filter(coin=coin)
            per = random.randint(40, 75)
            #value = value20[i]
            value = random.randint(0, 9)
            rem = value % 8
            for t in range(8):
                k = random.randint(0, 7)
                cat = cats[k] #select random coin
                per = random.randint(30, 70)
                if rem > 0:
                    if (value / 8 +1 ) * per * 0.01 > (value / 8+1) * (100 - per) * 0.01:
                        cat.votes_pro = cat.votes_pro + math.ceil((value / 8+1) * per * 0.01)
                        cat.votes_con = cat.votes_con + int((value / 8+1) * (100 - per) * 0.01)
                        cat.save()
                    else:
                        cat.votes_pro = cat.votes_pro + int((value / 8+1) * per * 0.01)
                        cat.votes_con = cat.votes_con + math.ceil((value / 8 + 1) * (100 - per) * 0.01)
                        cat.save()
                else:

                    if (value / 8) * per * 0.01 > (value / 8) * (100 - per) * 0.01:
                        cat.votes_pro = cat.votes_pro + math.ceil((value / 8 ) * per * 0.01)
                        cat.votes_con = cat.votes_con + int((value / 8) * (100 - per) * 0.01)
                        cat.save()
                    else:
                        cat.votes_pro = cat.votes_pro + int((value / 8) * per * 0.01)
                        cat.votes_con = cat.votes_con + math.ceil((value / 8) * (100 - per) * 0.01)
                        cat.save()
                rem = rem - 1
            coin.total_votes_pro = coin.total_votes_pro + math.ceil(value * per * 0.01)
            coin.total_votes_con = coin.total_votes_con + int(value * (100 - per) * 0.01)
            coin.total_votes = coin.total_votes_pro + coin.total_votes_con
            coin.save()
        print("1st Pass")
        for coin in coins[10:20]:
            cats = TotalRating.objects.filter(coin=coin)
            per = random.randint(40, 75)
            #value = value20[i]
            value = random.randint(0, 5)
            rem = value % 8
            for t in range(8):
                k = random.randint(0, 7)
                cat = cats[k] #select random coin
                per = random.randint(30, 70)
                if rem > 0:
                    if (value / 8 +1 ) * per * 0.01 > (value / 8+1) * (100 - per) * 0.01:
                        cat.votes_pro = cat.votes_pro + math.ceil((value / 8+1) * per * 0.01)
                        cat.votes_con = cat.votes_con + int((value / 8+1) * (100 - per) * 0.01)
                        cat.save()
                    else:
                        cat.votes_pro = cat.votes_pro + int((value / 8+1) * per * 0.01)
                        cat.votes_con = cat.votes_con + math.ceil((value / 8 + 1) * (100 - per) * 0.01)
                        cat.save()
                else:

                    if (value / 8) * per * 0.01 > (value / 8) * (100 - per) * 0.01:
                        cat.votes_pro = cat.votes_pro + math.ceil((value / 8 ) * per * 0.01)
                        cat.votes_con = cat.votes_con + int((value / 8) * (100 - per) * 0.01)
                        cat.save()
                    else:
                        cat.votes_pro = cat.votes_pro + int((value / 8) * per * 0.01)
                        cat.votes_con = cat.votes_con + math.ceil((value / 8) * (100 - per) * 0.01)
                        cat.save()
                rem = rem - 1
            coin.total_votes_pro = coin.total_votes_pro + math.ceil(value * per * 0.01)
            coin.total_votes_con = coin.total_votes_con + int(value * (100 - per) * 0.01)
            coin.total_votes = coin.total_votes_pro + coin.total_votes_con
            coin.save()
        print(" 2 nd Pass")
        for coin in coins[20:num_coins]:
            cats = TotalRating.objects.filter(coin=coin)
            per = random.randint(40, 75)
            #value = value20[i]
            value = random.randint(0, 2)
            rem = value % 8
            for t in range(8):
                k = random.randint(0, 7)
                cat = cats[k] #select random coin
                per = random.randint(30, 70)
                if rem > 0:
                    if (value / 8 +1 ) * per * 0.01 > (value / 8+1) * (100 - per) * 0.01:
                        cat.votes_pro = cat.votes_pro + math.ceil((value / 8+1) * per * 0.01)
                        cat.votes_con = cat.votes_con + int((value / 8+1) * (100 - per) * 0.01)
                        cat.save()
                    else:
                        cat.votes_pro = cat.votes_pro + int((value / 8+1) * per * 0.01)
                        cat.votes_con = cat.votes_con + math.ceil((value / 8 + 1) * (100 - per) * 0.01)
                        cat.save()
                else:

                    if (value / 8) * per * 0.01 > (value / 8) * (100 - per) * 0.01:
                        cat.votes_pro = cat.votes_pro + math.ceil((value / 8 ) * per * 0.01)
                        cat.votes_con = cat.votes_con + int((value / 8) * (100 - per) * 0.01)
                        cat.save()
                    else:
                        cat.votes_pro = cat.votes_pro + int((value / 8) * per * 0.01)
                        cat.votes_con = cat.votes_con + math.ceil((value / 8) * (100 - per) * 0.01)
                        cat.save()
                rem = rem - 1
            coin.total_votes_pro = coin.total_votes_pro + math.ceil(value * per * 0.01)
            coin.total_votes_con = coin.total_votes_con + int(value * (100 - per) * 0.01)
            coin.total_votes = coin.total_votes_pro + coin.total_votes_con
            coin.save()


        print("3rd pass")
        ##########################################################################################################

        # Loop through the categories and randomize the votes
        for category in categories:
            decision = random.randint(0, 4)
            if decision == 0 or decision == 1:
                newrating = CoinRating.objects.create(
                    coin=coin,
                    rater=adminuser,
                    category=category.category,
                    totalrating=category,
                    vote=True
                )
                newrating.save()
            elif decision == 2 or decision == 3:
                newrating = CoinRating.objects.create(
                    coin=coin,
                    rater=adminuser,
                    category=category.category,
                    totalrating=category,
                    vote=False
                )
                newrating.save()
            category.retally()
            category.save()

        # Retally the coin totals
        coin.retally()
        coin.save()
        #print(coin)
