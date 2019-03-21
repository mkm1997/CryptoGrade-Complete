from django.conf.urls import url
from . import views


# Declare the url patterns to visit via regex
urlpatterns = [

    # Basic website / administrative URLs
    url(r'^$', views.homepage, name='homepage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^disclaimer/$', views.disclaimer, name='disclaimer'),
    url(r'^contact/$', views.contact, name='contact'),

    # Coin-related URLs
    url(r'^coins/$', views.list_coins, name='list_coins'),
    url(r'^coins/(?P<ticker>[^/]+)/$', views.view_coin, name='view_coin'),

    # User profile related URLs
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/changepass/$', views.changepass, name='changepass'),
    url(r'^profile/delete/$', views.deleteprof, name='deleteprof'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^aj', views.ajaxcall, name="aj"),
    url(r'^update', views.Update, name="update"),
]
