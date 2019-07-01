from django import forms
from django.db import transaction

from .models import Organization, Membership

class OrganizationForm(forms.Form):
    name = forms.CharField(max_length=128, min_length=3, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea( attrs={'class':'form-control'}))


