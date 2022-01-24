from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }

class RawProductForm(forms.Form):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={"placeholder":"Title"}))
    description = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={"placeholder":"Description - Not Required"}))
    price = forms.DecimalField(required=True, label='', widget=forms.TextInput(attrs={"placeholder":"Price"}))