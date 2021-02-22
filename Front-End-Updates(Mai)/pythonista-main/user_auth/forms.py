from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length="25")
    last_name = forms.CharField(max_length="25")
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name',  'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length="25")
    last_name = forms.CharField(max_length="25")
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['linkedin', 'github', 'image']