from stats.models.models import Stats, Users
from rest_framework import viewsets
from rest_framework import permissions
from stats.serializers import StatsSerializer, UsersSerializer
from django.urls import resolve
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from stats.Services.stats_services import StatsService
import json

stats_service = StatsService()


class StatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited.
    """
    queryset = Stats.objects.all().order_by('-update_datetime')
    serializer_class = StatsSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print('============', resolve('/api/v1/stats/1/'))
        return Response(serializer.data)


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print('============', resolve('/api/v1/stats/1/'))
        return Response(serializer.data)
