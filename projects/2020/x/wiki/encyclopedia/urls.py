from django.urls import path

from . import views


urlpatterns = [

    #if path is empty run index function in encyclopedia/urls.py
    path("", views.index, name="index"),

    #If user visits /wiki/<anything> display page
    path("/wiki/<str:entry>", views.wiki, name="wiki")

]