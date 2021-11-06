from django import forms

from products.models import ProductModel


class ProductModelForm(forms.ModelForm):
	class Meta:
		model = ProductModel
		exclude = ['created_at']
