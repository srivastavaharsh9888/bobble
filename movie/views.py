from django.db.models import Sum
from rest_framework import generics

from datetime import datetime
from .models import Movie, UserScore
from .serializers import MovieSerializer, ScoreManagementSerializer


class LeadershipBoard(generics.ListAPIView):
    serializer_class = ScoreManagementSerializer

    def get_queryset(self):
        date_to_consider = self.request.query_params.get('date', datetime.today().strftime('%Y-%m-%d'))
        return UserScore.objects.filter(score_date=date_to_consider).values('user__username').annotate(total_score=Sum('score')).order_by('-total_score')

class ScoreManagement(generics.CreateAPIView):
    serializer_class = ScoreManagementSerializer

class MovieDetail(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()