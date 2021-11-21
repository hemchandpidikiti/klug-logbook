from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Attende

class AttendeFormIn(forms.ModelForm):
    class Meta:
        model = Attende
        fields = '__all__'
        exclude = ['out_time']

class AttendeFormOut(forms.ModelForm):
    class Meta:
        model = Attende
        fields = ['uid']
        #, 'date_out_time' widgets = {'date_out_time': forms.HiddenInput()}

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']