from stats.models.models import UserInfo
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions
from stats.serializers import AccountsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from stats.Services.board_services import BoardService
from stats.consts.swagger_params import board_get_list_params, board_post_params, board_put_params
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

    @swagger_auto_schema(request_body=board_post_params)
    def post(self, request):
        request_data = request.data
        result = board_service.set_board_and_records(request_data)
        return Response(result)

    @swagger_auto_schema(manual_parameters=board_get_list_params)
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
        result = board_service.delete_board(pk)
        return Response(result)

    @swagger_auto_schema(request_body=board_put_params)
    def put(self, request, pk):
        result = board_service.update_board(request.data, pk)
        return Response(result)
