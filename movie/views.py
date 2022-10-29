from django.db.models import Sum
from rest_framework import generics

from datetime import datetime
from .models import Movie, UserScore
from .serializers import MovieSerializer, ScoreManagementSerializer


class LeadershipBoard(generics.ListAPIView):
    serializer_class = ScoreManagementSerializer

    def get_queryset(self):
        date_to_consider = self.request.query_params.get('date', datetime.today().strftime('%Y-%m-%d'))
        return UserScore.objects.filter(score_date=date_to_consider).values('user__username').annotate(
            total_score=Sum('score')).order_by('-total_score')


class ScoreManagement(generics.CreateAPIView):
    serializer_class = ScoreManagementSerializer


class UserCentricDashboard(generics.ListAPIView):
    serializer_class = ScoreManagementSerializer
    lookup_field = None

    def get_queryset(self):
        date_to_consider = self.request.query_params.get('date', datetime.today().strftime('%Y-%m-%d'))
        username = self.request.query_params.get('username')
        user_score = UserScore.objects.filter(score_date=date_to_consider, user__username=username).values('user__username').annotate(
            total_score=Sum('score')).order_by('-total_score')
        if user_score:
            mid_score = user_score[0]['total_score']
            upper_user_score = UserScore.objects.filter(score_date=date_to_consider, user__username=username).values('user__username').annotate(
            total_score=Sum('score')).filter(total_score__gte=mid_score).order_by('-total_score')[:3]
            lower_user_score = UserScore.objects.filter(score_date=date_to_consider, user__username=username).values('user__username').annotate(
            total_score=Sum('score')).filter(total_score__lte=mid_score).order_by('-total_score')[:3]
            return upper_user_score
        return []


class MovieDetail(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()
