from gc import get_stats
from urllib import request
from stats.models import Stats
from rest_framework import viewsets
from rest_framework import permissions
from stats.serializers import StatsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stats.Services.stats_services import StatsService
import json
from stats.models import Stats

stats_service = StatsService()


class StatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited.
    """
    queryset = Stats.objects.all().order_by('-update_datetime')
    serializer_class = StatsSerializer
    permission_classes = [permissions.AllowAny]


class Statistics(APIView):
    def get(self, request: object, pk: int) -> str:
        try:
            stats = Stats.objects.get(pk=pk)
        except Stats.DoesNotExist:
            return Response(status=Http404)

        serializer = StatsSerializer(stats)
        data = serializer.data
        result = stats_service.get_statistics(data)

        return Response(result)
