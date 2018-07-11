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
    url(r'^index/mobiles/$', views.mobiles),

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

    url(r'^category/$', views.category),

    url(r'^post/category/$', views.category),
    
    #-- navigation around mobiles (edittedby sc)
    url(r'^index/mobiles.html/post-ad.html/$', views.redirectpostad),

    url(r'^index/mobiles.html/index/$', views.redirectIndex),
	
    url(r'postad/index/$', views.redirectIndex),
	
    url(r'^index/mobiles.html/signin.html/$', views.redirectSignin),
	
    url(r'^mobiles/index/$', views.redirectIndex),
	
    url(r'^mobiles/mobiles/$', views.redirectmobiles),
	
    url(r'^([^S]+)/([^S]+)/post-ad.html/$', views.redirectpostad),
    #end of edit

)
