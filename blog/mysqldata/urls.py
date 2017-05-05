from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	# General List of all Users
	# Pattern is :- /usr_list/data/
    url(r'^data/', views.display_usr, name = 'display_usr'),

    # Detail View of a User Produced as requested.
    # Pattern is :- /usr_list/<user_id>
    # <user_id>, variable which stores the natural number
    url(r'^(?P<user_id>[0-9]+)/$', views.detail_usr, name = 'detail_usr'),

    # Default URL to form page
    # Pattern :- /usr_list/
    
    url(r'^$', views.newuser, name = 'newuser'),

]