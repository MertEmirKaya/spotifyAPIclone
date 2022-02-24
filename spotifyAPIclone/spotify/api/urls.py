from django.urls import path,include
from .views import ArtistsListAPIView
urlpatterns = [
    path('artists/',ArtistsListAPIView.as_view())
]