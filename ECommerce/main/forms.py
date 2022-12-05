from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import ProductReview,UserAddressBook

""" Formulario de Login """
class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')

""" Formulario para hacer Revies """
class ReviewAdd(forms.ModelForm):
	class Meta:
		model=ProductReview
		fields=('review_text','review_rating')

""" Formulario de Direcciones """
class AddressBookForm(forms.ModelForm):
	class Meta:
		model=UserAddressBook
		fields=('address','mobile','status')

""" Formulario de Perfiles """
class ProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username')