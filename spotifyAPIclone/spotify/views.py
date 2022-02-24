
from .models import SpotifyToken
from django.http import HttpResponse
import requests
from requests import post
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.generics import ListAPIView
import datetime
from django.utils import timezone
from .credentials import client_id,client_secret,redirect_uri,base64Message
class Auth():

    def get_auth(request):
        url='https://accounts.spotify.com/api/token'
        response=requests.post(url=url,params={
            'grant_type':'client_credentials',
        },headers={
            'Authorization':'Basic '+base64Message,
            'Content-Type':'application/x-www-form-urlencoded',
        })
        access_token=response.json()['access_token']
        now=timezone.now()
        current_time = now.strftime("%H:%M:%S")
        expires_in=response.json()['expires_in']
        expires_at=now + datetime.timedelta(seconds=expires_in)
        expires_time=expires_at.strftime("%H:%M:%S")
        token_type=response.json()['token_type']
        user=request.user
        user_check=SpotifyToken.objects.filter(user=user)
        if user_check.exists():
            now=timezone.now()
            current_time = now.strftime("%H:%M:%S")
            if expires_time<current_time:
                SpotifyToken.objects.filter(user=request.user).update(access_token=access_token,expires_in=expires_in)

        else:
            SpotifyToken.objects.create(user=request.user,access_token=access_token,token_type=token_type,expires_in=expires_in)
        return HttpResponse(response)




