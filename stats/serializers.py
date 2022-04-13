from stats.models.models import Stats, Users
from rest_framework import serializers


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ['blockshots', 'create_datetime', 'create_user', 'offensive_rebounds', 'hustle_plays', 'memo',
                  'rebounds', 'scores', 'threepoints', 'update_datetime', 'update_user', 'assists', 'screen_assists', 'good_screens']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
