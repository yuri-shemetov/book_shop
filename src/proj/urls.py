"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('s-admin/', admin.site.urls, name='admin'),
    path('', include('shop.urls')),
    path('', include('directories.urls')),
    path('carts/', include('carts.urls', namespace='carts'), name='carts'),
    path('users/', include('users.urls', namespace='users'), name='users'),
    path('order/', include('orders.urls', namespace='orders'), name='order'),
    path('comments/', include('comments.urls', namespace='comments'), name='comments'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)