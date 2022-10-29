from django.contrib import admin

from .models import Movie, UserScore

admin.site.register(Movie)

admin.site.register(UserScore)