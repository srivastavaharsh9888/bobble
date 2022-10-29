from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=500)
    poster_path = models.CharField(max_length=500)
    language = models.CharField(max_length=250)
    overview = models.TextField()
    release_date = models.DateField()
    update_date = models.DateTimeField(auto_now=True)


class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.BigIntegerField(default=0)
    score_date = models.DateField()
    created = models.DateTimeField(auto_now=True)