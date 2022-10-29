from django.urls import path

from .views import MovieDetail, ScoreManagement, LeadershipBoard, UserCentricDashboard

urlpatterns = [
    path('submit_score/', ScoreManagement.as_view(), name='submitscore'),
    path('get_leadership_board/', LeadershipBoard.as_view(), name='leadershipboard'),
    path('get_usercentric_board/', UserCentricDashboard.as_view(), name='scoreboard'),
    path('movies/', MovieDetail.as_view(), name='moviedetail'),
]