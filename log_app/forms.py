from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Attende, Master
from django.forms import ModelForm, TextInput, EmailInput
class AttendeFormIn(forms.ModelForm):
    class Meta:
        model = Attende
        fields = '__all__'
        exclude = ['room_name', 'uname', 'in_time', 'out_time', 'authentication_type']

class AttendeFormOut(forms.ModelForm):
    class Meta:
        model = Attende
        fields = ['uid']
        #, 'date_out_time' widgets = {'date_out_time': forms.HiddenInput()}

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':"form-control", 'type':'password', 'style': 'width: 100%;', 'placeholder':'Enter password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':"form-control", 'type':'password', 'style': 'width: 100%;', 'placeholder':'re-Enter password'}),
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Enter Student ID or Employee ID'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;',
                'placeholder': 'User Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;',
                'placeholder': 'Enter Email'
                })
                
        }
class SaveForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['rfid_id']