import os
from django.contrib import auth
from django.db.models import Q
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from .models import *
import django.contrib.auth
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    username = request.session.get('username', "sign in")
    return render(request, 'index.html/', {'username': username})


def signin(request):
    return render(request, 'signin.html/')


def signup(request):
    return render(request, 'signup.html/')


def account(request):
    username = request.session.get('username', "sign in")
    user = User.objects.get(username=username)
    userid = user.id
    productList = Products.objects.filter(buyer=userid).order_by('productPrice')
    comments = Comments.objects.filter(owner=userid)
    return render(request, 'account.html/', {'productList': productList, 'username': username, 'comments': comments})


def comments(request):
    username = request.session.get('username', "sign in")
    return render(request, 'comments.html', {'username': username})


def comment(request):
    username = request.POST.get('title')
    user = User.objects.get(username=username)
    description = request.POST.get('description')
    comment = Comments(description=description, owner=user)
    comment.save()
    return HttpResponseRedirect('/account')


def mobiles(request, pageid, sortid):
    username = request.session.get('username', "sign in")

    # sort
    if sortid == '1':   # sort from high to low
        productList = Products.objects.filter(productCategory='1').order_by('productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)
    if sortid == '0':   # sort from low to high
        productList = Products.objects.filter(productCategory='1').order_by('-productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)

    return render(request, "mobiles.html/", {'productList': page, 'username': username})


def electronics(request, pageid, sortid):
    username = request.session.get('username', "sign in")

    if sortid == '1':
        productList = Products.objects.filter(productCategory='2').order_by('productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)
    if sortid == '0':
        productList = Products.objects.filter(productCategory='2').order_by('-productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)

    return render(request, "electronics-appliances.html/", {'productList': page, 'username': username})


def bikes(request, pageid, sortid):
    username = request.session.get('username', "sign in")

    if sortid == '1':
        productList = Products.objects.filter(productCategory='3').order_by('productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)
    if sortid == '0':
        productList = Products.objects.filter(productCategory='3').order_by('-productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)

    return render(request, "bikes.html/", {'productList': page, 'username': username})


def books(request, pageid, sortid):
    username = request.session.get('username', "sign in")

    if sortid == '1':
        productList = Products.objects.filter(productCategory='4').order_by('productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)
    if sortid == '0':
        productList = Products.objects.filter(productCategory='4').order_by('-productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)

    return render(request, "books.html/", {'productList': page, 'username': username})


def post(request):
    username = request.session.get('username', "sign in")
    return render(request, 'post.html/', {'username': username})


def single(request, productid):
    username = request.session.get('username', "sign in")
    product = Products.objects.get(id=productid)
    return render(request, 'singles.html/', {'product': product, 'username': username})


def categories(request):
    username = request.session.get('username', "sign in")
    return render(request, 'categories.html/', {'product': product, 'username': username})


# redirect
from django.http import HttpResponseRedirect


def redirectSignup(request):
    return HttpResponseRedirect('/signup')


def redirectsSignin(request):
    return HttpResponseRedirect('/signin')


def redirectSignin(request, pageid, sortid):
    return HttpResponseRedirect('/signin')


def redirectIndex(request):
    return HttpResponseRedirect('/index')


def redirectsIndex(request, sortid):
    return HttpResponseRedirect('/index')


def redirectsIndex(request, pageid, sortid):
    return HttpResponseRedirect('/index')


def redirectMobile(request):
    return HttpResponseRedirect('/mobiles')


def redirectPost(request):
    return HttpResponseRedirect('/post')


def redirectPosts(request, pageid, sortid):
    return HttpResponseRedirect('/post')


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


def logouts(request, sortid):
    django.contrib.auth.logout(request),
    return HttpResponseRedirect('/index')


def logouts(request, pageid, sortid):
    django.contrib.auth.logout(request),
    return HttpResponseRedirect('/index')


def search(request, pageid, sortid):
    username = request.session.get('username', "sign in")
    if request.method == 'GET':
        keywords = request.GET.get('Search')  # get the search key words
        if sortid == '1':
            productList = Products.objects.filter(Q(productName__icontains=keywords)
                                                  | Q(productInformation__icontains=keywords)).order_by('productPrice')
            paginator = Paginator(productList, 2)
            page = paginator.page(pageid)
        if sortid == '0':
            productList = Products.objects.filter(Q(productName__icontains=keywords)
                                                  | Q(productInformation__icontains=keywords)).order_by('-productPrice')
            paginator = Paginator(productList, 2)
            page = paginator.page(pageid)

        return render(request, "categories.html/", {'productList': page, 'username': username})


def redirectSingle(request, sortid, productid):
    return HttpResponseRedirect('/single')


def redirectSingle(request):
    return HttpResponseRedirect('/single')


# create a product when user post an item through post.html
def category(request):
    username = request.session.get('username', "sign in")
    productCategory = request.POST.get('selects')
    productName = request.POST.get('title')
    productPrice = request.POST.get('price')
    productInformation = request.POST.get('description')
    product = Products(productName=productName, productPrice=productPrice, productInformation=productInformation,
                       productCategory=productCategory, productImage=request.FILES.get('img'), buyer=request.user)
    product1 = Products()
    product.save()
    return render(request, 'post.html/', {'username': username})


def delete(request, productid):
    username = request.session.get('username', "sign in")
    user = User.objects.get(username=username)
    userid = user.id
    Products.objects.get(id=productid).delete()
    productList = Products.objects.filter(buyer=userid).order_by('productPrice')
    return render(request, 'account.html/', {'productList': productList, 'username': username})