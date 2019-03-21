import threading

from django.http import JsonResponse, Http404,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from CoinViewer.models import Coin, CoinRating, Account, TotalRating
import binascii
import requests
import base64
import re
from time import sleep
from threading import Thread
from django.core.management import call_command

########################################################################################################################
# Constants
########################################################################################################################
from django.views.decorators.csrf import csrf_exempt

CAPTCHA_KEY_LOGIN = "NkxlTlBWRVVBQUFBQUJBN1B1RkUxcEpUTVVkUW5OeHJCVmZ6aXdKUA=="
CAPTCHA_KEY_REGISTER = "NkxldFExRVVBQUFBQUIyVmJ6bE5qNGFYR3lJVnBUNDBxdlIzQVhaTQ=="

########################################################################################################################
# Utility functions
########################################################################################################################


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


########################################################################################################################
# Administrative and basic views
########################################################################################################################


def homepage(request):

    # Get the top 4 coins today
    top = Coin.objects.all().order_by("-pct_change_day")
    top4 = (top[0], top[1], top[2], top[3])
    bot4 = (top[len(top)-1], top[len(top)-2], top[len(top)-3], top[len(top)-4])
    coins = Coin.objects.all()
    num_coins = len(coins)
    sum = 0

    for coin in coins:
        sum = sum + coin.total_votes

    print(sum)

    for item in top4:
        item.pct_change_day = round(item.pct_change_day, 1)
        if item.pct_change_day == 0.0:
            item.pct_change_color = "black"
        else:
            item.pct_change_color = "rgb(80, 165, 80)"
    for item in bot4:
        item.pct_change_day = round(item.pct_change_day, 1)
        if item.pct_change_day == 0.0:
            item.pct_change_color = "black"
        else:
            item.pct_change_color = "rgb(217, 83, 79)"

    return render(request, 'CoinViewer/homepage.html', {"top4": top4, "bot4": bot4,"coins":num_coins,"sum":sum})


def about(request):
    return render(request, 'CoinViewer/about.html', {'title': "About - Cryptograde"})


def faq(request):
    return render(request, 'CoinViewer/faq.html', {'title': "FAQ - Cryptograde"})


def disclaimer(request):
    return render(request, 'CoinViewer/disclaimer.html', {'title': "Disclaimer - Cryptograde"})


def contact(request):
    return render(request, 'CoinViewer/contact.html', {'title': "Contact - Cryptograde"})


########################################################################################################################
# Coin rating views
########################################################################################################################


def list_coins(request):

    coins = Coin.objects.all()
    coins = coins.order_by('-market_cap')

    args = {
        'coins': coins,
        'title': "Coins - CryptoGrade"
    }

    return render(request, 'CoinViewer/coin_list.html', args)


def view_coin(request, ticker):

    # Obtain the coin from the DB
    coin = Coin.objects.filter(ticker=ticker)

    # If the coin doesn't exist then show an error page
    if not coin.exists():
        raise Http404()

    # Get the coin object from the queryset, associated totalratings, associated coinratings
    coin = coin.first()
    cats = TotalRating.objects.filter(coin=coin)
    cats = cats.order_by('priority')

    # If the user isn't authenticated, don't show the voting arrows (redirect to view_coin_anon)
    if not request.user.is_authenticated():
        args = {
            'exists': True,
            'coin': coin,
            'cats': cats,
        }
        return render(request, 'CoinViewer/coin_anonuser.html', args)

    # If the user is authenticated, obtain his coinratings
    ratings_all = CoinRating.objects.filter(coin=coin, rater=request.user)

    # Handle votes accordingly
    if request.method == 'POST':
        try:
            action = request.POST.get('action')
            category_id = request.POST.get('category_id')
            category = cats.get(pk=category_id)
        except ObjectDoesNotExist as exc:
            return JsonResponse({"bad_data_refresh": True})
        except KeyError as exc:
            return JsonResponse({"bad_data_refresh": True})

        if action == 'upvote':

            if ratings_all.filter(totalrating=category).exists():
                try:
                    # Get the CoinRating object
                    rating = ratings_all.get(totalrating=category)

                    # If the user had previously upvoted, they're deleting their upvote
                    if rating.vote:
                        rating.delete()
                        category.votes_pro = category.votes_pro - 1
                        coin.total_votes_pro = coin.total_votes_pro - 1

                    # If the user had previously downvoted, they're changing their vote to an upvote
                    elif not rating.vote:
                        rating.vote = True
                        rating.save()
                        category.votes_con = category.votes_con - 1
                        category.votes_pro = category.votes_pro + 1
                        coin.total_votes_con = coin.total_votes_con - 1
                        coin.total_votes_pro = coin.total_votes_pro + 1

                # If there's a glitch and multiple objects are generated, handle things accordingly
                except MultipleObjectsReturned as exc:
                    ratings_all.filter(totalrating=category).delete()
                    category.retally()
                    category.save()
                    coin.retally()
                    coin.save()
                    return JsonResponse({"bad_data_refresh": True})

            else:  # If the user hadn't had a vote for this category, they're upvoting it
                newrating = CoinRating.objects.create(coin=coin, rater=request.user, category=category.category,
                                                      totalrating=category, vote=True)
                newrating.save()
                category.votes_pro = category.votes_pro + 1
                coin.total_votes_pro = coin.total_votes_pro + 1

        elif action == 'downvote':

            if ratings_all.filter(totalrating=category).exists():
                try:
                    # Get the CoinRating object
                    rating = ratings_all.get(totalrating=category)

                    # If the user had previously downvoted, they're deleting their downvote
                    if not rating.vote:
                        rating.delete()
                        category.votes_con = category.votes_con - 1
                        coin.total_votes_con = coin.total_votes_con - 1

                    # If the user had previously upvoted, they're changing their vote to a downvote
                    elif rating.vote:
                        rating.vote = False
                        rating.save()
                        category.votes_pro = category.votes_pro - 1
                        category.votes_con = category.votes_con + 1
                        coin.total_votes_pro = coin.total_votes_pro - 1
                        coin.total_votes_con = coin.total_votes_con + 1

                # If there's a glitch and multiple objects are generated, handle things accordingly
                except MultipleObjectsReturned as exc:
                    ratings_all.filter(totalrating=category).delete()
                    category.retally()
                    category.save()
                    coin.retally()
                    coin.save()
                    return JsonResponse({"bad_data_refresh": True})

            else:  # If the user hadn't had a vote for this category, they're downvoting it
                newrating = CoinRating.objects.create(coin=coin, rater=request.user, category=category.category,
                                                      totalrating=category, vote=False)
                newrating.save()
                category.votes_con = category.votes_con + 1
                coin.total_votes_con = coin.total_votes_con + 1

        # Recalculate category and coin data
        category.recalculate()
        category.save()
        coin.recalculate()
        coin.save()

        # Return JSON to be rendered via AJAX callback
        data = {
            "bad_data_refresh": False,
            "votes_pro": category.votes_pro,
            "votes_con": category.votes_con,
            "px_green": category.px_green,
            "total_votes": coin.total_votes,
            "total_votes_pro": coin.total_votes_pro,
            "total_votes_con": coin.total_votes_con,
            "total_sentiment_pct": coin.total_sentiment_pct,
            "total_sentiment_pct_color": coin.total_sentiment_pct_color,
            "total_sentiment_descr": coin.total_sentiment_descr,
            "pct_chg_day": coin.pct_change_day,
            "pct_chg_color": coin.pct_change_color
        }
        return JsonResponse(data)

    # Populate cat_list with necessary 3-tuples
    cat_list = []
    for cat in cats:
        vote = ratings_all.filter(totalrating=cat)
        if vote.exists():
            vote = vote.first()
            cat_list.append((cat, True, vote))
        else:
            cat_list.append((cat, False, None))

    # Pass necessary information as arguments
    args = {
        'exists': True,
        'coin': coin,
        'cat_list': cat_list,
        'meta': "Vote on and view stats for {} on CryptoGrade, the leading community sentiment tracking and analysis platform for cryptocurrencies.".format(coin.name),
        'title': "({}) {} - CryptoGrade".format(coin.ticker, coin.name)
    }

    return render(request, 'CoinViewer/coin.html', args)


########################################################################################################################
# Authentication views
########################################################################################################################


def login_page(request):

    # TODO - Forgot your password?
    # TODO - Maybe even forgot your username?

    # First up - if the user is already authenticated, redirect to profile
    if request.user.is_authenticated():
        return redirect('profile')

    # Check for valid form input
    if request.method == "POST":
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        captcha = request.POST.get('g-recaptcha-response')

        # First check to see if the captcha is valid
        cap_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                "secret": base64.b64decode(CAPTCHA_KEY_LOGIN),
                #"secret" : "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe",
                "response": captcha,
                "remoteip": get_client_ip(request)
            }
        )  # If the captcha wasn't valid, render error message
        if not cap_response.json()['success']:
            return render(request, 'CoinViewer/login.html', {'bad_captcha': True, 'title': "Login - Cryptograde"})

        # Then check authentication credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'CoinViewer/login.html', {'acct_inactive': True, 'title': "Login - Cryptograde"})
        else:
            return render(request, 'CoinViewer/login.html', {'invalid_creds': True, 'title': "Login - Cryptograde"})

    return render(request, 'CoinViewer/login.html', {'title': "Login - Cryptograde"})


def register(request):

    # First up - if the user is already authenticated, redirect to profile
    if request.user.is_authenticated():
        return redirect('profile')

    # Check for valid form input
    if request.method == "POST":
        username = request.POST.get('inputUsername')
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        password_confirmation = request.POST.get('inputPasswordConfirm')
        captcha = request.POST.get('g-recaptcha-response')

        # First check to see if the captcha is valid
        cap_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                #"secret": base64.b64decode(CAPTCHA_KEY_REGISTER),
                "secret": "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe",
                "response": captcha,
                "remoteip": get_client_ip(request)
            }
        )  # If the captcha wasn't valid, render error message
        if not cap_response.json()['success']:
            return render(request, 'CoinViewer/register.html', {'bad_captcha': True, 'title': "Register - Cryptograde"})

        # Check: Is the username currently in use?
        if User.objects.filter(username=username).exists():
            return render(request, 'CoinViewer/register.html', {'takenusername': True, 'title': "Register - Cryptograde"})

        # Check: Is the username valid?
        usr_pattern = re.compile("^[\w.@+-]+$")
        if not usr_pattern.match(username):
            return render(request, 'CoinViewer/register.html', {'invalidusername': True, 'title': "Register - Cryptograde"})

        # Check: Is the username between 3 and 32 characters long, inclusive?
        if len(username) < 3 or len(username) > 32:
            return render(request, 'CoinViewer/register.html', {'tooshortusername': True, 'title': "Register - Cryptograde"})

        # Check: Is the email currently in use?
        if User.objects.filter(email=email).exists():
            return render(request, 'CoinViewer/register.html', {'takenemail': True, 'title': "Register - Cryptograde"})

        # Check: Is the email valid?
        eml_pattern = re.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
        if not eml_pattern.match(email):
            return render(request, 'CoinViewer/register.html', {'invalidemail': True, 'title': "Register - Cryptograde"})

        # Check: Are the two passwords identical?
        if password != password_confirmation:
            return render(request, 'CoinViewer/register.html', {'passwordmismatch': True, 'title': "Register - Cryptograde"})

        # Check: Is the password at least 8 characters long?
        if len(password) < 8:
            return render(request, 'CoinViewer/register.html', {'tooshortpassword': True, 'title': "Register - Cryptograde"})

        # If all checks have passed, register the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        acct = Account.objects.create(user=user)
        acct.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('profile')

    return render(request, 'CoinViewer/register.html', {'title': "Register - Cryptograde"})


def logout_page(request):

    # First up - if user isn't authenticated, redirect to login
    if not request.user.is_authenticated():
        return redirect('login_page')

    # Log the user out and return to login page
    logout(request)
    return redirect('login_page')


def profile(request):

    # First up - if user isn't authenticated, redirect to login
    if not request.user.is_authenticated():
        return redirect('login_page')

    # Get the user's ratings for display and pass into view
    ratings = CoinRating.objects.filter(rater=request.user).order_by('coin')
    if len(ratings) == 0:
        return render(request, 'CoinViewer/profile_view.html', {'ratings': ratings, 'noratings': True, 'title': "Profile - Cryptograde"})
    else:
        return render(request, 'CoinViewer/profile_view.html', {'ratings': ratings, 'title': "Profile - Cryptograde"})


def changepass(request):

    # First up - if the user isn't authenticated, redirect to login
    if not request.user.is_authenticated():
        return redirect('login_page')

    # If it's a POST request, check for valid data
    if request.method == "POST":
        current1 = request.POST.get('inputCurrentPass')
        current2 = request.POST.get('inputCurrentPass2')
        new1 = request.POST.get('inputNewPass')
        new2 = request.POST.get('inputNewPass2')

        # Check - are the passwords all the same?
        if current1 != current2 or new1 != new2:
            return render(request, 'CoinViewer/changepass.html', {'mismatch': True})

        # Check - are the credentials valid?
        authtest = authenticate(username=request.user.username, password=current1)
        if authtest is None:
            return render(request, 'CoinViewer/changepass.html', {'invalid_creds': True})

        # Check - are the passwords all the same?
        if len(new1) < 8:
            return render(request, 'CoinViewer/changepass.html', {'tooshortpassword': True})

        # If all checks passed, then change the password
        request.user.set_password(new1)
        request.user.save()
        return render(request, 'CoinViewer/changepass.html', {'changed': True})

    return render(request, 'CoinViewer/changepass.html')


def deleteprof(request):

    # First up - if the user isn't authenticated, redirect to login
    if not request.user.is_authenticated():
        return redirect('login_page')

    # If it's a POST request, check for valid data
    if request.method == "POST":
        password = request.POST.get('inputPass')

        # Check - are the credentials valid?
        authtest = authenticate(username=request.user.username, password=password)
        if authtest is None:
            return render(request, 'CoinViewer/deleteprof.html', {'invalid_creds': True})

        # If the credentials were valid, then delete all CoinRatings associated with the user, then the user
        CoinRating.objects.filter(rater=request.user).delete()  # Changes will be picked up on the next retally
        request.user.delete()
        return redirect('homepage')

    return render(request, 'CoinViewer/deleteprof.html')


###############################################AjaxCall################################


FLAG =0
@csrf_exempt
def ajaxcall(request):

    coins = Coin.objects.all()
    num_coins = len(coins)
    sum = 0
    #call_command('generate_votes') #it call the custom database mangement code

    for coin in coins:
        sum = sum + coin.total_votes
    print(sum)
    return HttpResponse(sum)

##########For updating the database
@csrf_exempt
def Update(request):
    print("I am uppdating")

    call_command('generate_votes')
    call_command('recalculate_all')

    return HttpResponse("<h1>successfully updated data base,</h1>")





