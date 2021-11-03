from django.urls import path

from products.views import ProductTemplateView, TableTemplateView, ProfileTemplateView

app_name = 'products'

urlpatterns = [
	path('', ProductTemplateView.as_view(), name='product'),
	path('table/', TableTemplateView.as_view(), name='table'),
	path('profile/', ProfileTemplateView.as_view(), name='profile'),
	# path('', ProductTemplateView.as_view()),
]
