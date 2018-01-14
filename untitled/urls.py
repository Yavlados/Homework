"""My_HW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from my_app.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/main', permanent=False), name='index'),
    url(r'^main', main, name='main_url'),
    url(r'^login', login, name='login_url'),
    url(r'^logout', logout, name='logout_url'),
    url(r'^registration2', registration2, name='registration2_url'),
    url(r'^registration', registration, name='registration_url'),
    url(r'^tovar_show', tovar_show, name='tovar_show_url'),
    url(r'^feedback_add', fb_add, name='feedback_add_url'),
    url(r'^tovar', TovarList.as_view(), name='tovar_url'),
    url(r'^good_add', good_add, name='good_add_url'),
    url(r'^shop', ShopList.as_view(), name='shop_url'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)