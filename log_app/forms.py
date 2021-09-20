from django.forms import ModelForm
from django import forms
from .models import Attende

class AttendeFormIn(forms.ModelForm):
    class Meta:
        model = Attende
        fields = '__all__'
        exclude = ['date_out_time']

class AttendeFormOut(forms.ModelForm):
    class Meta:
        model = Attende
        fields = ['uid', 'date_out_time']
        widgets = {'date_out_time': forms.HiddenInput()}