from django.shortcuts import render
from django.views.generic import TemplateView


class ProductTemplateView(TemplateView):
	# template_name = 'QR admin temp/dashboard.html'
	template_name = 'user temp/index.html'


class TableTemplateView(TemplateView):
	template_name = 'QR admin temp/basic-table.html'


class ProfileTemplateView(TemplateView):
	template_name = 'QR admin temp/profile.html'


