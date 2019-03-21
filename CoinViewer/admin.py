from django.contrib import admin
from . import models

########################################################################################################################
# TotalRating admin actions
########################################################################################################################


def recalculate(modeladmin, request, queryset):
    for trating in queryset:
        trating.recalculate()
        trating.save()


class TotalRatingAdmin(admin.ModelAdmin):
    actions = [recalculate, ]

########################################################################################################################
# RatingCategory admin actions
########################################################################################################################


def add_category_to_coins(modeladmin, request, queryset):
    coins = models.Coin.objects.all()
    for rcat in queryset:
        for coin in coins:
            if not models.TotalRating.objects.filter(category=rcat, coin=coin).exists():
                tr = models.TotalRating.objects.create(
                    category=rcat,
                    coin=coin,
                    priority=rcat.priority,
                )
                tr.save()


def remove_category_from_coins(modeladmin, request, queryset):

    # TODO - Remove user-submitted ratings in removed category

    coins = models.Coin.objects.all()
    for rcat in queryset:
        for coin in coins:
            if models.TotalRating.objects.filter(category=rcat, coin=coin).exists():
                models.TotalRating.objects.filter(category=rcat, coin=coin).get().delete()


class RatingCategoryAdmin(admin.ModelAdmin):
    actions = [add_category_to_coins, remove_category_from_coins, ]


########################################################################################################################
# Model registration
########################################################################################################################

admin.site.register(models.Account)
admin.site.register(models.TotalRating, TotalRatingAdmin)
admin.site.register(models.RatingCategory, RatingCategoryAdmin)
admin.site.register(models.CoinRating)
admin.site.register(models.Coin)
