from stats.models import Stats
from rest_framework import viewsets
from rest_framework import permissions
from stats.serializers import StatsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited.
    """
    queryset = Stats.objects.all().order_by('-update_datetime')
    serializer_class = StatsSerializer
