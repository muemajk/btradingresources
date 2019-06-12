from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from ecommerce.models import Member, Product, ProductCompany, ProductCatergory, Cart
from django.utils import timezone
from .signals import user_logged_in
from decimal import Decimal
import string
from random import *

from .forms import Contactform, LoginForm, RegisterForm , UserForm, Checkoutform, Productnumber
# Create your views here.
def admin_page(request):
    return redirect('/admin')




#this form is used by registered users to sign in
def login_page(request):
    logout(request)
    form = LoginForm(request.POST or None)

    template = loader.get_template('members/login.html')
    context = {
        'form' : form
    }
    print('User logged in')
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            user_logged_in.send(user.__class__, instance=user, request = request)
            context['form'] = LoginForm()
            if request.user.is_authenticated:
                currentUser = request.user
                userid = currentUser.id
                request.session['userID'] = userid
                request.session['Usern']= currentUser.username
                print(request.session['userID'])
                return redirect('/ecommerce/store/')
        else:
            
            print("Error!") 
    return HttpResponse(template.render(context,request))



def index(request):
    usez = None
    context = {
        'user_name': usez,
        'times' : timezone.now(),
           }
    if request.user.is_authenticated:
        username = request.user.username
        context['user_name']= username
        print(username)
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context,request))


#this page view displays all workers and admins on the the website
def membership_view(request):
    usez = None
    context = {
        'user_name': usez,
        'times' : timezone.now(),
           }
    if request.user.is_authenticated:
        username = request.user.username
        context['user_name']= username
        print(username)
    template = loader.get_template('membership.html')
    return HttpResponse(template.render(context,request))


def company_view(request):
    template = loader.get_template('company.html') 
    usez = None
    context = {
        'user_name': usez,
        'times' : timezone.now(),
           }
    if request.user.is_authenticated:
        username = request.user.username
        context['user_name']= username
        
    return HttpResponse(template.render(context,request))


def logout_view(request):
    logout(request)
    try:
        del request.session['member_id']
        del request.session['userID']
    except KeyError:
        pass
    return redirect('/ecommerce')


def biotec_view(request):
    template = loader.get_template('biotec.html') 
    usez = None
    context = {
        'user_name': usez,
        'times' : timezone.now(),
           }
    if request.user.is_authenticated:
        username = request.user.username
        context['user_name']= username
        
    return HttpResponse(template.render(context,request))


def flint_view(request):
    template = loader.get_template('flintwood.html') 
    usez = None
    context = {
        'user_name': usez,
        'times' : timezone.now(),
           }
    if request.user.is_authenticated:
        username = request.user.username
        context['user_name']= username
        
    return HttpResponse(template.render(context,request))


def tk_view(request):
    template = loader.get_template('tktitan.html') 
    usez = None
    context = {
        'user_name': usez,
        'times' : timezone.now(),
           }
    if request.user.is_authenticated:
        username = request.user.username
        context['user_name']= username
        
    return HttpResponse(template.render(context,request))
