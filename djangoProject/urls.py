"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from nivi import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('option',views.option,name='option'),
    path('contact',views.contact,name='contact'),
    path('add',views.add,name='add'),
    path('contact2',views.contact2,name='contact2'),
    path('add2',views.add2,name='add2'),
    path('option2',views.option2,name='option2'),
    path('source',views.source,name='source'),
    path('audio',views.audio,name='audio'),
    path('source2',views.source2,name='source2'),
    path('audio2',views.audio2,name='audio2'),
    path('features',views.features,name='features'),
    path('video',views.video,name='video'),
    path('record',views.record,name='record'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})

]




