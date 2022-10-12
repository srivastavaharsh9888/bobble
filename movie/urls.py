from django.urls import path

from .views import MovieDetail

urlpatterns = [
    path('api/movies/', MovieDetail.as_view(), name='moviedetail'),
]