from django.conf.urls import url
from . import views

urlpatterns = (

    # url to index page
    url(r'^index/$', views.index),

    url(r'^login/index/$', views.redirectIndex),

    # url to sign up page
    url(r'^signup/$', views.signup),

    # url to sign in page
    url(r'^signin/$', views.signin),

    # url to mobile page
    url(r'^index/mobiles/$', views.redirectMobile),

    url(r'^mobiles/$', views.mobiles),

    # url to electronics page
    url(r'^index/electronics/$', views.electronics),

    # # url to post item page
    # url(r'^post/$', views.post),

    # redirect the url to sign up page
    url(r'^login/signup/$', views.redirectSignup),

    url(r'^signin/signup/$', views.redirectSignup),

    # redirect the url to sign in page
    url(r'^signup/signin/$', views.redirectSignin),

    # redirect the url to sign in page
    url(r'^signin/signin/$', views.redirectSignin),

    # redirect the url to index page
    url(r'^signin/index/$', views.redirectIndex),

    url(r'^index/index/$', views.redirectIndex),

    # redirect the url to index page
    url(r'^signup/index/$', views.redirectIndex),

    url(r'^back/$', views.back),

    url(r'^index/signin/$', views.redirectSignin),

    # url(r'^main/$', views.main),
    #
    # url(r'^main/login/$', views.login),
    #
    # url(r'^showmain/$', views.showmain),

    url(r'^index/quit/$', views.logout),

    url(r'^login/quit/$', views.logout),

    url(r'^register/quit/$', views.logout),

    url(r'^register/$', views.register),

    url(r'^login/$', views.login),

    url(r'^post/$', views.post),

    url(r'^index/post/$', views.redirectPost),

    url(r'^post/post/$', views.redirectPost),

    url(r'^post/index/$', views.redirectIndex),

    url(r'^post/quit/$', views.logout),

    # url(r'^category/$', views.category),
    #
    # url(r'^post/category/$', views.category),

    url(r'^mobiles/(\d+)/$', views.mobiles),

    url(r'^mobiles/(\d+)/quit/$', views.logouts),

    url(r'^index/mobiles/(\d+)/$', views.mobiles),

    url(r'^index/mobiles/(\d+)/index/$', views.redirectsIndex),



)
