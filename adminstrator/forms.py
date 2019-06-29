from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django_countries.fields import CountryField
from .models import freightRate


class FrieghtForm(forms.ModelForm):
	class Meta:
		model = freightRate
		fields = ['From_source_to_Port_freight','Port_freight', 'From_port_to_destination_freight', 'Product_types' ]


	Origin=  CountryField(blank_label='(select country)').formfield()

	Destination_Country=  CountryField(blank_label='(select country)').formfield()


	

	Metric= forms.CharField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_metric',
				'placeholder':'What is the product unit metric(Kilogram, Grams or liters)'
			 }
		 )		
	)


	Minimum_Quantity_Sent= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'Minimum amount of product sent'
			 }
		 )		
	)

	Maximum_Quantity_Sent= forms.IntegerField(
				widget=forms.TextInput(
					attrs={'class' : 'form-control',
					'id': 'form_source',
					'placeholder':'Maximum amount of product sent'
				 }
			 )		
		)

	Minimum_Quantity_Recieved= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'Minimum amount of product recieved'
			 }
		 )		
	)


	Maximum_Quantity_Recieved= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'Maximum amount of product recieved'
			 }
		 )		
	)


	Origin_Clearing_Agent= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_type',
				'placeholder':'Agent fee for clearing the products at its Origin'
			 }
		 )		
	)


	Destination_Clearing_Agent= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_type',
				'placeholder':'Agent fee for clearing the products at the Destination'
			 }
		 )		
	)




	Total_cost= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'What is the total cost of the products'
			 }
		 )		
	)



	Unit_cost= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'What is the unit cost per product'
			 }
		 )		
	)



	Mark_up_Rate= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'What is the product mark up cost'
			 }
		 )		
	)



	Source_tax= forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'What is the product source country tax'
			 }
		 )		
	)


	Destination_tax = forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'What is the product Destination country tax'
			 }
		 )		
	)



	Source_Other_tax = forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'What is the product Destination country tax'
			 }
		 )		
	)


	Destination_Other_tax = forms.IntegerField(
			widget=forms.TextInput(
				attrs={'class' : 'form-control',
				'id': 'form_source',
				'placeholder':'What is the product Destination country tax'
			 }
		 )		
	)


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		conpass = self.cleaned_data.get("confirm_password")

		if conpass != password:
			raise forms.ValidationError("The passwords must match!")
			print(password)
			print(conpass)
		return data


	def clean_username(self):
		username = self.cleaned_data.get('username')
		ps = User.objects.filter(username=username)
		if ps.exists():
			raise forms.ValidationError("An account with this username exists")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		pe = User.objects.filter(email = email)
		if pe.exists():
			raise forms.ValidationError("An account with this Email Address exists")
		return email








