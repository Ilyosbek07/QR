from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView

from products.forms import ProductModelForm
from products.models import ProductModel, CategoryModel


class ProductListView(ListView):
	template_name = 'user temp/index.html'
	model = ProductModel
	paginate_by = 3

	def get_queryset(self):
		qs = ProductModel.objects.order_by('-pk')
		q = self.request.GET.get('q', None)
		cat = self.request.GET.get('cat')

		if q:
			qs = qs.filter(title__icontains=q)

		if cat:
			qs = qs.filter(category__title__icontains=cat)
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['categories'] = CategoryModel.objects.order_by('pk')
		return context



class ProductTemplateView(TemplateView):
	# template_name = 'QR admin temp/dashboard.html'
	template_name = 'user temp/index.html'


class TableTemplateView(TemplateView):
	template_name = 'QR admin temp/edit  product.html'


class ProfileTemplateView(TemplateView):
	template_name = 'QR admin temp/profile.html'


class ProductCreateView(CreateView):
	# model = ProductModel
	template_name = 'QR admin temp/add product.html'
	form_class = ProductModelForm

	# def form_valid(self, form):
	# 	form.instance.post = get_object_or_404(ProductModel, pk=self.kwargs.get('pk'))
	# 	return super().form_valid(form)

	def get_success_url(self):
		return reverse('products:add_product')
# return reverse('products:add_product', kwargs={'pk': self.kwargs.get('pk')})
# class CardListView(ListView):
# 	template_name = 'card.html'

	# def get_queryset(self):
	# 	return ProductModel.get_from_cart(self.request)

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)

		# context['products'] = ProductModel.get_from_cart(self.request)

		# return context