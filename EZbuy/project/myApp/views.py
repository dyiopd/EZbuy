import os
from django.contrib import auth
from django.db.models import Q
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from .models import *
import django.contrib.auth
from django.core.paginator import Paginator


# Display a error page
#  This page will be shown if you miss something when you try to post your item
#  @return error.html An error information
#  @return username The username of current user
def error(request):
    username = request.session.get('username', "sign in")
    return render(request, 'error.html/', {'username': username})


# Go to EZbuy website's homepage.
#  This web page will automatically get username from session and display it on the right upper corner.
#  @return username The username of current user
#  @return index.html A home page of this website
#  @note this web application needs to sign in, so that you can view products and post your items
def index(request):
    username = request.session.get('username', "sign in")
    return render(request, 'index.html/', {'username': username})


# Go to signin page.
#  This web page is used for customer to sign in
#  @return signin.html A signin html web page
def signin(request):
    return render(request, 'signin.html/')


# Go to sign up page.
#  @return signup.html A signup html web page
def signup(request):
    return render(request, 'signup.html/')


# Go to account page.
#  This web page will automatically get username from session and display it on the right upper corner.
#  We will use this username to get all the comments and products that related to this user.
#  These information will display on account web page.
#  In this web page you also can delete the product post by you.
#  @return account.html A account html web page
#  @return productList A product list that store all the products related to this user
#  @return username The user name of current user
#  @return comments The comments list that store all the comments this user received.
def account(request):
    username = request.session.get('username', "sign in")
    user = User.objects.get(username=username)
    userid = user.id
    productList = Products.objects.filter(buyer=userid).order_by('productPrice')
    comments = Comments.objects.filter(owner=userid)
    return render(request, 'account.html/', {'productList': productList, 'username': username, 'comments': comments})


# Go to comment page.
#  This web page will automatically get username from session and display it on the right upper corner.
#  In this page, you need to enter the username of the person you want to make comments on.
#  @return comments.html A comments html web page
#  @return username The username of current user
def comments(request):
    username = request.session.get('username', "sign in")
    return render(request, 'comments.html', {'username': username})


# It a post method.
#  This method will get and store all the comment information entered by user from POST method.
#  These information is passed from comments html page.
#  @return '/account' Redirect to a account html web page
def comment(request):
    username = request.POST.get('title')
    # try:
    #     user = models.User.objects.get(username=username)
    # except:
    #     return render(request, 'userNotFound.html/')

    if User.objects.filter(username=username):
        user = User.objects.get(username=username)
        description = request.POST.get('description')
        acomment = Comments(description=description, owner=user)
        acomment.save()
        return HttpResponseRedirect('/account')

    # user = User.objects.get(username=username)
    # description = request.POST.get('description')
    # acomment = Comments(description=description, owner=user)
    # acomment.save()
    # return HttpResponseRedirect('/account')
    return render(request, 'userNotFound.html/')

# Go to mobiles web page.
#  This web page will display all mobiles products, and the current username on the right upper conner.
#  In this web page, you can search products, sort products by price.
#  @param pageid The page number you currently in
#  @param sorid The way you want to sort.
#  @return mobiles.html A mobiles html page
#  @return productList Stores all the mobile product
#  @return username The current user
#  @return sortid The way you want to sort
#  @note For sort id, 1 means sort by price from high to low. 2 means sort by price from low to high.
def mobiles(request, pageid, sortid):
    username = request.session.get('username', "sign in")
    productList = Products.objects.filter(productCategory='1').order_by('productPrice')
    paginator = Paginator(productList, 2)
    page = paginator.page(pageid)
    # sort
    if sortid == '1':  # sort from high to low
        productList = Products.objects.filter(productCategory='1').order_by('productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)
    if sortid == '0':  # sort from low to high
        productList = Products.objects.filter(productCategory='1').order_by('-productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)

    return render(request, "mobiles.html/", {'productList': page, 'username': username, 'sortid': sortid})


# Go to electronics web page.
#  This web page will display all electronics products, and the current username on the right upper conner.
#  In this web page, you can search products, sort products by price.
#  @param pageid The page number you currently in
#  @param sorid The way you want to sort.
#  @return electronics.html A electronics html page
#  @return productList Stores all the electronics product
#  @return username The current user
#  @return sortid The way you want to sort
#  @note For sort id, 1 means sort by price from high to low. 2 means sort by price from low to high.
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

    return render(request, "electronics-appliances.html/",
                  {'productList': page, 'username': username, 'sortid': sortid})


#  Go to bikes web page.
#  This web page will display all bikes products, and the current username on the right upper conner.
#  In this web page, you can search products, sort products by price.
#  @param pageid The page number you currently in
#  @param sorid The way you want to sort.
#  @return bikes.html A bikes html page
#  @return productList Stores all the bikes product
#  @return username The current user
#  @return sortid The way you want to sort
#  @note For sort id, 1 means sort by price from high to low. 2 means sort by price from low to high.
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

    return render(request, "bikes.html/", {'productList': page, 'username': username, 'sortid': sortid})


# Go to books web page.
#  This web page will display all books products, and the current username on the right upper conner.
#  In this web page, you can search products, sort products by price.
#  @param pageid The page number you currently in
#  @param sorid The way you want to sort.
#  @return books.html A books html page
#  @return productList Stores all the books product
#  @return username The current user
#  @return sortid The way you want to sort
#  @note For sort id, 1 means sort by price from high to low. 2 means sort by price from low to high.
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

    return render(request, "books.html/", {'productList': page, 'username': username, 'sortid': sortid})


# Go to post web page
#  In this page, you can post your items
#  @return psot.html A post html page
def post(request):
    username = request.session.get('username', "sign in")
    return render(request, 'post.html/', {'username': username})


# Go to singles web page
#  This page will display the detailed information of a specific product, and the sellers information.
#  @param productid The id of specific product
#  @return singles.html a singles html page
#  @return product A specific product
#  @return username The user name of current user
#  @return commentList The comments this seller has received
def single(request, productid):
    username = request.session.get('username', "sign in")
    product = Products.objects.get(id=productid)
    person = product.buyer
    commentList = Comments.objects.filter(owner=person)
    return render(request, 'singles.html/', {'product': product, 'username': username, 'commentList': commentList})


# Go to categories web page.
#  This web page will be used when user use search function, on this page, it will display results
#  In this web page, you can search products, sort products by price.
#  @param pageid The page number you currently in
#  @param sorid The way you want to sort.
#  @param keywords The characters that you entered in search section
#  @return categories.html A category html page
#  @return page Stores all result product in specific page
#  @return username The current user
#  @return sortid The way you want to sort
#  @return keywords The characters that you entered in search section
def categories(request, pageid, sortid, keywords):
    print('keyword', keywords)
    username = request.session.get('username', "sign in")
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

    return render(request, "categories.html/",
                  {'productList': page, 'username': username, 'sortid': sortid, 'keyword': keywords})

# Go to categories web page.
#  This web page will be used when user use search function and enter a whitespace as a keyword,
#  on this page, it will display all products in our database.
#  In this web page, you can search products, sort products by price.
#  @param pageid The page number you currently in
#  @param sorid The way you want to sort.
#  @return categories.html A category html page
#  @return page Stores all result product in specific page
#  @return username The current user
#  @return sortid The way you want to sort
def allcategory(request, pageid, sortid):
    username = request.session.get('username', "sign in")
    if sortid == '1':
        productList = Products.objects.all().order_by('productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)
    if sortid == '0':
        productList = Products.objects.all().order_by('-productPrice')
        paginator = Paginator(productList, 2)
        page = paginator.page(pageid)
    return render(request, "categories.html/",
                  {'productList': page, 'username': username, 'sortid': sortid})


# redirect
from django.http import HttpResponseRedirect


# Redirect to sign up web page
def redirectSignup(request):
    return HttpResponseRedirect('/signup')


# Redirect to sign in web page
def redirectsSignin(request):
    return HttpResponseRedirect('/signin')


# Redirect to sign in web page
#  @param pageid The page number you currently in
#  @param sortid The way your product sorted
def redirectSignin(request, pageid, sortid):
    return HttpResponseRedirect('/signin')


# Redirect to home web page
def redirectIndex(request):
    return HttpResponseRedirect('/index')


# Redirect to home web page
#  @param sortid The way your product sorted
def redirectsIndex(request, sortid):
    return HttpResponseRedirect('/index')


# Redirect to home web page
#  @param pageid The page number you currently in
#  @param sortid The way your product sorted
def redirectsIndex(request, pageid, sortid):
    return HttpResponseRedirect('/index')


# Redirect to mobiles web page
def redirectMobile(request):
    return HttpResponseRedirect('/mobiles')


# Redirect to post web page
def redirectPost(request):
    return HttpResponseRedirect('/post')


# Redirect to post web page
#  @param pageid The page number you currently in
#  @param sortid The way your product sorted
def redirectPosts(request, pageid, sortid):
    return HttpResponseRedirect('/post')


# Redirect to home web page
#  this method is been used when user complete his registration, and it will automatically go to home page.
def back(request):
    username = request.POST.get('Name')
    request.session['username'] = username
    return HttpResponseRedirect('/index')


# It's a method for registration
#  It will get and store all information entered by user from POST method, and create a user model.
#  @return index.html A home page html page
def register(request):
    username = request.POST.get('Name')
    # request.session['username'] = username
    # user = User.objects.get(username=username)
    password = request.POST.get('Password')
    email = request.POST.get('Email')

    if User.objects.filter(username=username):
        return render(request, 'userExist.html/')

    registerAdd = User.objects.create_user(username=username, password=password, email=email)
    request.session['username'] = username
    if not registerAdd:  # didn't register
        return render(request, 'index.html/')
    else:  # register successfully
        request.session['username'] = username
        return HttpResponseRedirect('/index')


# It'a method for log in
#  It will get username and password from POST method, and check whether they are matched.
#  @return index.html A home page
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


# It's a logout method
#  It allow user to quit his account
def logout(request):
    django.contrib.auth.logout(request),
    return HttpResponseRedirect('/index')


# It's a logout method
#  It allow user to quit his account.
#  @param sortid The way your product sorted
def logouts(request, sortid):
    django.contrib.auth.logout(request),
    return HttpResponseRedirect('/index')


# It's a logout method
#  This logout method will be used when user is not in home page.
#  @param pageid The page number you currently in
#  @param sortid The way your product sorted
def logouts(request, pageid, sortid):
    django.contrib.auth.logout(request),
    return HttpResponseRedirect('/index')


# It'a search method
#  It allow user search everything in our website
#  @param pageid The page number you currently in
#  @param sortid The way your product sorted
#  @return categories.html The search results will be displayed on categories page
#  @return page Stores all result product in specific page
#  @return username The current user
#  @return sortid The way you want to sort
#  @return keywords The characters that you entered in search section
#  @note the default page number is 1, and the default sort method is from low to high
def search(request, pageid, sortid):
    username = request.session.get('username', "sign in")
    if request.method == 'GET':

        if request.GET.get('Search')[0] != " ":
            keywords = request.GET.get('Search')  # get the search key words

        # if request.GET.get('Search')[0] == " " and request.GET.get('Search')[1] != " ":
        #     keywords = request.GET.get('Search').replace(" ", "")
        # if request.GET.get('Search').strip()=="":

        if request.GET.get('Search')[0] == " ":
            keywords = request.GET.get('Search').replace(" ", "")
            productList = Products.objects.all()
            paginator = Paginator(productList, 2)
            page = paginator.page(pageid)
            return HttpResponseRedirect("/allcategory/1/0/",
                                        {'productList': page, 'username': username, 'sortid': sortid})
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

        return render(request, "categories.html/", {'productList': page, 'username': username, 'keyword': keywords,
                                                    'sortid': sortid})


# Redirect to single page
#  This method will be used when user not at home page
#  @param pageid The page number you currently in
#  @param sortid The way your product sorted
def redirectSingle(request, sortid, productid):
    return HttpResponseRedirect('/single')


# Redirect to single page
def redirectSingle(request):
    return HttpResponseRedirect('/single')


# It's a method to create a product
#  This method will get all the required information about the product through POST method, and store the product
#  in database.
#  @return post.html A post html page
#  @return username The username of current user
#  @not if you miss something information about your product, it will give you a error message
# create a product when user post an item through post.html
def category(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    productCategory = request.POST.get('selects')
    productName = request.POST.get('title')
    productPrice = request.POST.get('price')
    productInformation = request.POST.get('description')
    try:
        number = float(productPrice)
    except ValueError:
        return HttpResponseRedirect('/error')
    if "-" not in request.POST.get('price'):
        product = Products(productName=productName, productPrice=productPrice, productInformation=productInformation,
                           productCategory=productCategory, productImage=request.FILES.get('img'), buyer=user)
        product.save()
        return HttpResponseRedirect('/index', {'username': username})
    else:
        return HttpResponseRedirect('/error')


# It'a delete method that allow user to delete their own posts.
#  @param productid The id of the product that will be deleted
#  @return account.html A account html page
#  @return productList The product list that contains all the products related to current user
#  @return username The username of current user
def delete(request, productid):
    username = request.session.get('username', "sign in")
    user = User.objects.get(username=username)
    userid = user.id
    Products.objects.get(id=productid).delete()
    productList = Products.objects.filter(buyer=userid).order_by('productPrice')
    return render(request, 'account.html/', {'productList': productList, 'username': username})
