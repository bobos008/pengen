"""gzpengen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from indexs import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.index),
    url(r'^boutique/', views.boutique),
    url(r'^concerning/', views.concerning),
    url(r'^customizedc/', views.customizedc),
    url(r'^addcustom/', views.addcustom),
    url(r'^detail/(\w+)/(\d+)/', views.detail),
    url(r'^indulgence/', views.indulgence),
    url(r'^itineray/', views.itinerary),
    url(r'^knowledge/', views.knowledge),
    url(r'^popular/', views.popular),
    url(r'^scenic/', views.scenic),
    url(r'^strategy/', views.strategy),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
