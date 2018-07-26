from django.conf.urls import url
from . import views

urlpatterns = (

    url(r'^$', views.redirectIndex),

    # url(r'^categories/$', views.categories),

    url(r'^search/$', views.search),

    url(r'^search/(\d+)/(\d+)/$', views.search),

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

    # redirect the url to sign up page
    url(r'^login/signup/$', views.redirectSignup),

    url(r'^signin/signup/$', views.redirectSignup),

    # redirect the url to sign in page
    url(r'^signup/signin/$', views.redirectsSignin),

    # redirect the url to sign in page
    url(r'^signin/signin/$', views.redirectsSignin),

    # redirect the url to index page
    url(r'^signin/index/$', views.redirectIndex),

    url(r'^index/index/$', views.redirectIndex),

    # redirect the url to index page
    url(r'^signup/index/$', views.redirectIndex),

    url(r'^back/$', views.back),

    url(r'^index/signin/$', views.redirectsSignin),

    url(r'^index/quit/$', views.logout),

    url(r'^quit/$', views.logout),

    url(r'^login/quit/$', views.logout),

    url(r'^register/quit/$', views.logout),

    url(r'^register/$', views.register),

    url(r'^login/$', views.login),

    url(r'^post/$', views.post),

    url(r'^index/post/$', views.redirectPost),

    url(r'^post/post/$', views.redirectPost),

    url(r'^post/index/$', views.redirectIndex),

    url(r'^post/quit/$', views.logout),

    url(r'^category/$', views.category),

    url(r'^post/category/$', views.redirectIndex),

    url(r'^index/mobiles/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/mobiles/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/mobiles/(\d+)/(\d+)/$', views.mobiles),

    url(r'^mobiles/(\d+)/(\d+)/$', views.mobiles),

    url(r'^mobiles/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^mobiles/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^index/mobiles/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^mobiles/(\d+)/(\d+)/quit/$', views.logouts),

    url(r'^index/mobiles/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^mobiles/(\d+)/(\d+)/post/$', views.redirectPosts),

    url(r'^single/$', views.single),

    url(r'^single/(\d+)/$', views.single),

    url(r'^single/1/$', views.single),

    url(r'^single/1$', views.single),

    url(r'^index/mobiles/0/singles/(\d+)/$', views.single),

    url(r'^mobiles/0/singles/(\d+)/$', views.single),

    url(r'^index/account/$', views.account),

    url(r'^account/$', views.account),

    url(r'^delete/(\d+)/$', views.delete),

    url(r'^comments/$', views.comments),

    # electronics urls
    url(r'^index/electronics/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/electronics/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/electronics/(\d+)/(\d+)/$', views.electronics),

    url(r'^electronics/(\d+)/(\d+)/$', views.electronics),

    url(r'^electronics/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^electronics/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^index/electronics/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^electronics/(\d+)/(\d+)/quit/$', views.logouts),

    url(r'^index/electronics/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^electronics/(\d+)/(\d+)/post/$', views.redirectPosts),

    url(r'^index/electronics/0/singles/(\d+)/$', views.single),

    # bikes urls
    url(r'^index/bikes/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/bikes/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/bikes/(\d+)/(\d+)/$', views.bikes),

    url(r'^bikes/(\d+)/(\d+)/$', views.bikes),

    url(r'^bikes/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^bikes/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^index/bikes/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^bikes/(\d+)/(\d+)/quit/$', views.logouts),

    url(r'^index/bikes/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^bikes/(\d+)/(\d+)/post/$', views.redirectPosts),

    url(r'^index/bikes/0/singles/(\d+)/$', views.single),

    # books urls
    url(r'^index/books/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/books/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/books/(\d+)/(\d+)/$', views.books),

    url(r'^books/(\d+)/(\d+)/$', views.books),

    url(r'^books/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^books/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^index/books/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^books/(\d+)/(\d+)/quit/$', views.logouts),

    url(r'^index/books/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^books/(\d+)/(\d+)/post/$', views.redirectPosts),

    url(r'^index/books/0/singles/(\d+)/$', views.single),

    # categories urls
    url(r'^index/categories/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/categories/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^index/categories/(\d+)/(\d+)/$', views.categories),

    url(r'^categories/(\d+)/(\d+)/$', views.categories),

    url(r'^categories/(\d+)/(\d+)/index/$', views.redirectsIndex),

    url(r'^categories/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^index/categories/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^categories/(\d+)/(\d+)/quit/$', views.logouts),

    url(r'^index/categories/(\d+)/(\d+)/signin/$', views.redirectSignin),

    url(r'^categories/(\d+)/(\d+)/post/$', views.redirectPosts),

    url(r'^index/categories/0/singles/(\d+)/$', views.single),


)
