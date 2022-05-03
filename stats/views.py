from stats.models.models import UserInfo
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from stats.Services.board_services import BoardService
from stats.Services.dashboard_services import DashboardService
from stats.consts.swagger_params import board_get_list_params, board_post_params, board_put_params
from stats.serializers import BoardRequestSerializer
from stats.exceptions import InvalidUserRequestException
import json

board_service = BoardService()
dashboard_service = DashboardService()


class BoardsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=board_post_params)
    def post(self, request):
        request_data = request.data
        create_user = request.user.user_id
        result = board_service.set_board_and_records(request_data, create_user)
        return Response(result)

    @swagger_auto_schema(query_serializer=BoardRequestSerializer)
    def get(self, request):
        current_user = request.user.user_id
        request_data = {param_set[0]: param_set[1] for param_set in request.GET.items()}
        request_data['create_user'] = current_user
        result = board_service.get_board_list(request_data)
        return Response(result)


class BoardsDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        result = board_service.get_board_detail(pk)
        return Response(result)

    def delete(self, request, pk):
        result = board_service.delete_board(pk)
        return Response(result)

    @swagger_auto_schema(request_body=board_put_params)
    def put(self, request, pk):
        update_user = request.user.user_id
        result = board_service.update_board(request.data, pk, update_user)
        return Response(result)


class DashboardRecentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            current_user = request.user.user_id
            result = dashboard_service.get_dashboard_recent(current_user)
        except:
            raise InvalidUserRequestException()
        return Response(result)
