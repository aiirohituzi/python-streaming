"""audioStream URL Configuration

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
from streaming.views import getAudio
from streaming.views import selectGetAudio
from streaming.views import upload
from streaming.views import delete
from streaming.views import musicList
from streaming.views import musicUpload
from streaming.views import randomPlay

from streaming import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'audios', views.AudiosViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^getAudio/$', getAudio, name='getAudio'),
    url(r'^selectGetAudio/$', selectGetAudio, name='selectGetAudio'),
    url(r'^upload/$', upload, name='upload'),
    url(r'^delete/$', delete, name='delete'),
    url(r'^list/$', musicList, name='music_list'),
    url(r'^musicUpload/$', musicUpload, name='musicUpload'),
    url(r'^randomPlay/$', randomPlay, name='randomPlay'),
]