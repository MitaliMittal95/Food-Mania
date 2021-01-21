from django.core import validators
from django import forms
from .models import Truck


class AddShowTruck(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['name', 'location','opentime','closetime']
        widgets = {
            'name': forms.TextInput(attrs={'class' :'form-control'}),
            'location': forms.TextInput(attrs={'class' :'form-control'}),
            'opentime': forms.TextInput(attrs={'class' :'form-control','type':'time'}),
            'closetime': forms.TextInput(attrs={'class' :'form-control', 'type':'time'}),
        }
        