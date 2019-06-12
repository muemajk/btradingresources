from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from orders.models import FlintwoodOrders, BiotechOrders, TktitanOrders
from django.utils import timezone

from decimal import Decimal
import string
from random import *





#this page view will display all orders made
def index(request):
    template = loader.get_template('ecommerce/members/Userdetails.html')


    return HttpResponse(template.render(context,request))


def orders(request):
    currentUser = request.session['userID'] 
    try:
        memeber = Member.objects.filter(Userid=currentUser)
        for mem in memeber:
            meme = mem.id
            memphone = mem.phone_number
            memcountry = mem.country
            memphysical_address = mem.physical_address
    except  AttributeError as error:
        return redirect('/ecommerce/logout/')
        print(error)
    form = Checkoutform(request.POST or None)
    ordercart = Cart.objects.filter(Member_ID=meme)

    context = {
        'phone': memphone,
        'country': memcountry,
        'address':  memphysical_address,
        'form': form,
        'ordersize': 0,
    }    

    if form.is_valid():
        username = form.cleaned_data.get("cardcode")
    
    for order in ordercart:
        sizeord = len(ordercart)
        context['ordersize'] = sizeord

    template = loader.get_template('ecommerce/products/cart.html')
    return HttpResponse(template.render(context,request))





