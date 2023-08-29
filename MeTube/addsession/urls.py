from django.urls import path 
from . import views

urlpatterns = [
    path("", views.addsession, name="addsession")
]