import os
from django.contrib import auth
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from .models import *
import django.contrib.auth


# Create your views here.

def index(request):
    username = request.session.get('username', "sign in")
    print(request.user.id)
    return render(request, 'index.html/', {'username': username})


def signin(request):
    return render(request, 'signin.html/')


def signup(request):
    return render(request, 'signup.html/')


def mobiles(request):
    return render(request, "mobiles.html/")


def electronics(request):
    return render(request, 'electronics-appliances.html/')


def post(request):
    username = request.session.get('username', "sign in")
    return render(request, 'post.html/', {'username': username})

def postad(request):
	return render(request, 'post-ad.html/')


# redirect
from django.http import HttpResponseRedirect


def redirectSignup(request):
    return HttpResponseRedirect('/signup')


def redirectSignin(request):
    return HttpResponseRedirect('/signin')


def redirectIndex(request):
    return HttpResponseRedirect('/index')

#added by sc
def redirectpostad(request):
	return HttpResponseRedirect('/postad')
	
def redirectmobiles(request):
    return HttpResponseRedirect('/mobiles')
#edit end


def back(request):
    username = request.POST.get('Name')
    request.session['username'] = username
    return HttpResponseRedirect('/index')


def register(request):
    username = request.POST.get('Name')
    # request.session['username'] = username
    password = request.POST.get('Password')
    email = request.POST.get('Email')
    registerAdd = User.objects.create_user(username=username, password=password, email=email)

    if not registerAdd:  # didn't register
        return render(request, 'kids.html/')
    else:  # register successfully
        request.session['username'] = username
        return HttpResponseRedirect('/index')


def login(request):
    username = request.POST.get('Name')
    password = request.POST.get('Password')
    re = auth.authenticate(username=username, password=password)

    if re is not None:  # if username and password matches the data in database
        auth.login(request, re)  # login successfully
        request.session['username'] = username
        return HttpResponseRedirect('/index')  # jump to homepage
    else:  # there is no such data in database
        return render(request, 'signin.html', {'login_error': 'username or password error'})  # display error message
    return render(request, 'signin.html')


def logout(request):
    django.contrib.auth.logout(request),
    return HttpResponseRedirect('/index')


def category(request):
    username = request.session.get('username', "sign in")
    productCategory = request.POST.get('selects')
    productName = request.POST.get('title')
    productInformation = request.POST.get('description')
    product = Products(productName=productName, productInformation=productInformation,
                       productCategory=productCategory, productImage=request.FILES.get('img'), buyer=request.user)
    product.save()
    return render(request, 'post.html/', {'username': username})

# def main(request):
#     username = request.session.get('name', "log in")
#     return render(request, 'main.html', {'username': username})
#
#
# def login(request):
#     return render(request, 'login.html')
#
#
# def showmain(request):
#     username = request.POST.get('username')
#     request.session['name'] = username
#     return HttpResponseRedirect('/main')
