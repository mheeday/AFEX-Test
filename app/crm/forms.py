from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['cid', 'first_name', 'last_name', 'country_code', 'email', 'address', 'phone']

class UpdateWalletForm(forms.Form):
    amount = forms.FloatField(required=True)