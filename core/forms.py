from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =['image', 'product_name', 'description','stock', 'minimum_order', 'price']
