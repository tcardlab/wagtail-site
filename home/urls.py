from django.conf.urls import url
from django.contrib import admin

from . import views as home_views
admin.autodiscover()
# a urls.py in app is good for self contained apps or ones 
# you want to pass on. als doesnt clog the main urls.py
urlpatterns = [
	url(r'^getQuora2', home_views.getQuora2, name="getQuora2"),
]
