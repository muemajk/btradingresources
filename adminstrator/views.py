from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .forms import FrieghtForm
from .models import freightRate
from Users.models import Client
from django.contrib.auth.models import User

# Create your views here.
def freight_view(request):
	if request.user.is_authenticated:
	    currentUser = request.user
	else:
	    return redirect('/Users/login/')

	template = loader.get_template('admin/freight.html')
	fform = FrieghtForm(request.POST or None)
	
	
	context ={
		
	    'user_name': currentUser.username,
        'times' : timezone.now(),
        'fform' : fform,
        
        
	}

	if fform.is_valid():
		ptype = fform.cleaned_data.get('Product_types')
		source = fform.cleaned_data.get('Origin')
		desti = fform.cleaned_data.get('Destination_Country')
		means = fform.cleaned_data.get('Port_freight')
		sourcemeans = fform.cleaned_data.get('From_source_to_Port_freight')
		desmeans = fform.cleaned_data.get('From_port_to_destination_freight')
		metric = fform.cleaned_data.get('Metric')
		minsent = fform.cleaned_data.get('Minimum_Quantity_Sent')
		maxsent = fform.cleaned_data.get('Maximum_Quantity_Sent')
		minrecieve = fform.cleaned_data.get('Minimum_Quantity_Recieved')
		maxrecieve = fform.cleaned_data.get('Maximum_Quantity_Recieved')
		orgagent = fform.cleaned_data.get('Origin_Clearing_Agent')
		destagent = fform.cleaned_data.get('Destination_Clearing_Agent')		
		tcost = fform.cleaned_data.get('Total_cost')
		ucost = fform.cleaned_data.get('Unit_cost')
		markup = fform.cleaned_data.get('Mark_up_Rate')
		stax = fform.cleaned_data.get('Source_tax')
		dtax = fform.cleaned_data.get('Destination_tax')
		sotax = fform.cleaned_data.get('Source_Other_tax')
		dotax = fform.cleaned_data.get('Destination_Other_tax')




		newrate = freightRate(Source=source, Destination=desti,Port_freight= means,From_source_to_Port_freight=sourcemeans,From_port_to_destination_freight=desmeans,metric=metric, MiniQuantitySent=minsent,MaxQuantitySent=maxsent, MiniQuantityRecieved=minrecieve,MaxQuantityRecieved=maxrecieve, Total_cost= tcost, Unit_cost  = ucost,Sourcetax=stax, Destinationtax= dtax,Sourceothertax= sotax,Destinationothertax= dotax,MarkupRate=markup,Product_types=ptype, DestinAgent=destagent, OriginAgent=orgagent,  )
		newrate.save()
		return HttpResponseRedirect('/adminstrator/freightrate/')
	return HttpResponse(template.render(context,request))

usr = get_user_model()
def freight(request):
	if request.user.is_authenticated:
	    currentUser = request.user
	else:
	    return redirect('/Users/login/')

	template = loader.get_template('admin/freightview.html')
	fform = FrieghtForm(request.POST or None)
	
	
	context ={
		
	    'user_name': currentUser.username,
        'times' : timezone.now(),
        
        'freightrate_content': freightRate.objects.all()
        
	}

	
	return HttpResponse(template.render(context,request))



def product_view(request):
	pass

def suppliers_view(request):
	pass


usr = get_user_model()
def buyers_view(request):
	if request.user.is_authenticated:
	    currentUser = request.user
	else:
	    return redirect('/Users/login/')

	template = loader.get_template('admin/users.html')
	fform = FrieghtForm(request.POST or None)
	Userz =User.objects.all()
	print(Userz)
	context ={
		
	    'user_name': currentUser.username,
        'times' : timezone.now(),
        'usr' : User.objects.all(),
        'user_content': Client.objects.all(),
        
	}
	return HttpResponse(template.render(context,request))
def order_view(request):
	pass



def delete_user_view(request, pk,pk2):
	User.objects.filter(username=pk).delete()
	Client.objects.filter(id=pk2).delete()
	return HttpResponseRedirect('/adminstrator/users/')


def delete_frieght_view(request,pk):
	freightRate.objects.filter(id=pk).delete()
	return HttpResponseRedirect('/adminstrator/freightrate/')	