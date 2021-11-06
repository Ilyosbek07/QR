from django.urls import path

from products.views import ProductTemplateView, TableTemplateView, ProfileTemplateView, ProductCreateView, \
	ProductListView

app_name = 'products'

urlpatterns = [
	path('', ProductListView.as_view(), name='product'),
	# path('', ProductTemplateView.as_view(), name='product'),
	path('table/', TableTemplateView.as_view(), name='table'),
	path('profile/', ProfileTemplateView.as_view(), name='profile'),
	path('add_products/', ProductCreateView.as_view(), name='add_product'),
	# path('', ProductTemplateView.as_view()),
]
