from django.conf.urls import include, url
from django.contrib import admin

from . import views as search_views
admin.autodiscover()

#a urls.py in app is good for self contained apps or ones 
#you want to pass on. als doesnt clog the main urls.py
urlpatterns = [
	url(r'^getQuora/', search_views.getQuora, name="getQuora"),
]