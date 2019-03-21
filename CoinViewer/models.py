from __future__ import division
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    # This represents a single person who can rate a coin multiple times
    user = models.OneToOneField(User)

    # Field for account verification
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Coin(models.Model):

    # This data comes straight from CoinMarketCap API
    name = models.CharField(max_length=32)
    cmc_id = models.CharField(max_length=128, default="unknown")
    ticker = models.CharField(max_length=8)
    price_usd = models.FloatField(default=0.0)
    market_cap = models.FloatField(default=0.0)
    info_updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    # Each coin is going to have a total rollup rating
    total_votes = models.IntegerField(default=0)
    total_votes_pro = models.IntegerField(default=0)
    total_votes_con = models.IntegerField(default=0)
    total_sentiment_pct = models.FloatField(default=50.00)
    total_sentiment_pct_color = models.CharField(max_length=8, default="#595959")
    total_sentiment_descr = models.CharField(max_length=32, default="Neutral")
    total_rank = models.IntegerField(default=0)

    # Data for percentage changes
    pct_change_day = models.FloatField(default=0.0)
    pct_day_ago = models.FloatField(default=0.0)
    pct_change_color = models.CharField(max_length=8, default="black")

    def __str__(self):
        return self.name

    def recalculate(self):
        votes_total = self.total_votes_pro + self.total_votes_con
        self.total_votes = votes_total
        if votes_total == 0:  # To avoid divide by zero error
            self.total_sentiment_pct = 50.00
            self.total_sentiment_descr = "Neutral"
            self.total_sentiment_pct_color = "#98981a"
        else:
            self.total_sentiment_pct = round((100 * round((self.total_votes_pro / float(votes_total)), 4)), 2)
            int_sentiment_pct = int(self.total_sentiment_pct)
            if int_sentiment_pct <= 20:
                self.total_sentiment_descr = "Overwhelmingly Negative"
                self.total_sentiment_pct_color = "#af3434"
            elif int_sentiment_pct < 45:
                self.total_sentiment_descr = "Negative"
                self.total_sentiment_pct_color = "#987419"
            elif int_sentiment_pct <= 55:
                self.total_sentiment_descr = "Neutral"
                self.total_sentiment_pct_color = "#98981a"
            elif int_sentiment_pct < 80:
                self.total_sentiment_descr = "Positive"
                self.total_sentiment_pct_color = "#749819"
            else:
                self.total_sentiment_descr = "Overwhelmingly Positive"
                self.total_sentiment_pct_color = "#229819"
        self.pct_change_day = round(self.total_sentiment_pct - self.pct_day_ago, 2)
        if self.pct_change_day < 0:
            self.pct_change_color = "#af3434"
        elif self.pct_change_day == 0:
            self.pct_change_color = "black"
        else:
            self.pct_change_color = "#229819"

    def retally(self):
        trs = TotalRating.objects.filter(coin=self)
        pos_count = 0
        neg_count = 0
        for tr in trs:
            pos_count += tr.votes_pro
            neg_count += tr.votes_con
        self.total_votes_pro = pos_count
        self.total_votes_con = neg_count
        self.recalculate()

    def save_daily_percent(self):
        self.pct_day_ago = self.total_sentiment_pct
        self.pct_change_day = round(self.total_sentiment_pct - self.pct_day_ago, 2)


class RatingCategory(models.Model):

    # Rating key information
    category_name = models.CharField(max_length=32, default="Category")
    pos_name = models.CharField(max_length=32, default="Pos")
    neg_name = models.CharField(max_length=32, default="Neg")
    priority = models.IntegerField(default=5)
    tooltip = models.CharField(max_length=1024, default="Generic Tooltip Text")

    def __str__(self):
        return self.category_name


class TotalRating(models.Model):

    # TotalRatings are going to be many-to-one with both RatingCategories and Coins
    category = models.ForeignKey(RatingCategory)
    priority = models.IntegerField(default=5)  # Lifted directly from category priority
    coin = models.ForeignKey(Coin)

    # Key information is going to include the calculated statistic and votes in favor and against
    calculated_score = models.FloatField(default=0.5)
    px_green = models.IntegerField(default=50)
    px_red = models.IntegerField(default=50)
    votes_pro = models.IntegerField(default=0)
    votes_con = models.IntegerField(default=0)

    def __str__(self):
        combo = self.coin.name + " (" + self.category.category_name + ")"
        return combo

    def recalculate(self):
        votes_total = self.votes_pro + self.votes_con
        if votes_total == 0:  # To avoid divide by zero error
            votes_total += 1
            self.calculated_score = 0.50
            self.px_green = 50
            self.px_red = 50
        else:
            self.calculated_score = self.votes_pro / float(votes_total)
            self.px_green = int(self.calculated_score * 100)
            self.px_red = 100 - self.px_green

    def retally(self):
        crs = CoinRating.objects.filter(totalrating=self)
        pos_count = 0
        neg_count = 0
        for cr in crs:
            if cr.vote:
                pos_count += 1
            else:
                neg_count += 1
        self.votes_pro = pos_count
        self.votes_con = neg_count
        self.recalculate()


class CoinRating(models.Model):

    # Each CoinRating is many-to-one with a Coin, Person, TotalRating, and RatingCategory
    coin = models.ForeignKey(Coin)
    rater = models.ForeignKey(User)
    category = models.ForeignKey(RatingCategory)
    totalrating = models.ForeignKey(TotalRating)

    # Key information is merely a NullBooleanField containing the user's vote along with time info
    vote = models.BooleanField()

    def __str__(self):
        return "{}, {}, {}".format(self.coin.name, self.category.category_name, self.vote)
