from stats.models.models import UserInfo
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions
from stats.serializers import AccountsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from stats.Services.board_services import BoardService
from stats.Services.dashboard_services import DashboardService
from stats.Services.user_services import UserService
from stats.consts.swagger_params import board_get_list_params, board_post_params, board_put_params, account_post_params
import json

board_service = BoardService()
dashboard_service = DashboardService()
user_service = UserService()


class AccountsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=account_post_params)
    def post(self, request):
        try:
            data = json.loads(request.body)
            result = user_service.set_account(data)
            return Response(result)

        except:
            raise ValueError("잘못된 입력입니다.")


class BoardsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=board_post_params)
    def post(self, request):
        request_data = request.data
        result = board_service.set_board_and_records(request_data)
        return Response(result)

    @swagger_auto_schema(manual_parameters=board_get_list_params)
    def get(self, request):
        request_data = {param_set[0]: param_set[1] for param_set in request.GET.items()}
        request_data['create_user'] = 'hsjo'
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
        result = board_service.update_board(request.data, pk)
        return Response(result)


class DashboardRecentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        test_user_id = 'kbjang'
        result = dashboard_service.get_dashboard_recent(test_user_id)
        return Response(result)
