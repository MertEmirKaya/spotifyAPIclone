from urllib import request, response
from rest_framework.generics import ListAPIView
import requests
from spotify.models import SpotifyToken
from rest_framework.response import Response
class ArtistsListAPIView(ListAPIView):
    def get(self, request,):
        user_model=SpotifyToken.objects.first()
        
        url='https://api.spotify.com/v1/playlists/1iGDxe9EpZ4kXzFvCXf7V1?si=8d5814f981e44954'
        token=user_model.token_type+' '+user_model.access_token
        response=requests.get(url=url,headers={
            'Authorization':token
        }).json()
        return Response(data=response)
