from django.conf.urls import url
from django.contrib import admin
from .views import scrape,index

urlpatterns=[
    url(r'^views/',scrape,name='scrape'),
    url(r'^views/',index,name='index'),
]
