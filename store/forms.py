from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
