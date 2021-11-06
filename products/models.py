from django.db import models
from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Mahsulot Turi'


class ProductModel(models.Model):
	name = models.CharField(max_length=255)
	price = models.TextField()
	description = RichTextField()
	picture = models.ImageField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	product_cat = models.OneToOneField(
		CategoryModel,
		related_name='products',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Mahsulot'
		verbose_name_plural = 'Mahsulotlar'
