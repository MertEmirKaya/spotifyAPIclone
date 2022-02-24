import django
from django.urls import path,include
from .views import Auth


urlpatterns = [
    path('',Auth.get_auth)
]