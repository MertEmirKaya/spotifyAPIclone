from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SpotifyToken(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    access_token=models.CharField(max_length=150)
    expires_in=models.IntegerField(default=0)
    token_type=models.CharField(max_length=50)
