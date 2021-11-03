from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from products.views import ProductTemplateView

# urlpatterns = [
# 	path('ckeditor/', include('ckeditor_uploader.urls')),
# 	path('api/', include('rest_framework.urls')),
# ]
#
# urlpatterns += i18n_patterns(
# 	path('accounts/', include('auth1.urls', namespace='auth1')),
# 	path('admin/', admin.site.urls),
# 	path('service/', include('service.urls', namespace='service')),
# 	path('profile/', include('users.urls', namespace='profile')),
# 	path('order/', include('order.urls', namespace='order')),
# 	path('post/', include('post.urls', namespace='post')),
# 	path('', include('products.urls', namespace='products')),
# 	path('api/', include('api.urls', namespace='api')),
# )
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('products.urls', namespace='products')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
