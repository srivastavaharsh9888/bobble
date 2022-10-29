from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import Movie, UserScore


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields='__all__'


class ScoreManagementSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=500)

    def validate_username(self, value):
        user = get_object_or_404(User, username=value)
        return user

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        ret['user'] = ret['username']
        ret.pop('username')
        return ret

    def to_representation(self, instance):
        if hasattr(self, 'initial_data'):
           return {"username": self.initial_data['username'], "score": instance.score, "score_date": instance.score_date}
        return instance
    class Meta:
        model = UserScore
        fields = ['score', 'score_date', 'username']