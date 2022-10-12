from rest_framework import generics

from .models import Movie
from .serializers import MovieSerializer


class MovieDetail(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()