from stats.models import Stats
from rest_framework import serializers


class StatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stats
        fields = ['blockshots', 'create_datetime', 'create_user', 'offensive_rebounds', 'hustle_plays', 'memo',
                  'rebounds', 'scores', 'stat_id', 'threepoints', 'update_datetime', 'update_user', 'assists', 'screen_assists', 'good_screens']
