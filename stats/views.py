from stats.models.models import UserInfo
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions
from stats.serializers import AccountsSerializer
from django.urls import resolve
from rest_framework.views import APIView
from rest_framework.response import Response
from stats.Services.board_services import BoardService
import json

board_service = BoardService()


class AccountsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stats to be viewed or edited.
    """
    queryset = UserInfo.objects.all().order_by('-create_datetime')
    serializer_class = AccountsSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BoardsView(APIView):
    permission_classes = [permissions.AllowAny]

    board_param = [
        openapi.Parameter(
            'start_date',
            openapi.IN_QUERY,
            description="test manual param",
            type=openapi.FORMAT_DATE
        ),
        openapi.Parameter(
            'end_date',
            openapi.IN_QUERY,
            description="test manual param",
            type=openapi.FORMAT_DATE
        ),
    ]

    def post(self, request):
        request_data = request.data
        result = board_service.set_board_and_records(request_data)
        return Response(result)

    @swagger_auto_schema(manual_parameters=board_param)
    def get(self, request):
        request_data = request.data
        request_data['create_user'] = 'hsjo'
        result = board_service.get_board_list(request_data)
        return Response(result)


class BoardsDetailView(APIView):
    def get(self, request, pk):
        result = board_service.get_board_detail(pk)
        return Response(result)

    def delete(self, request, pk):
        return Response(0)
