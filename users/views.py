from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.serializers import UserCreateSerializer, UserLoginSerializer, LoginRequestSerializer, LoginResponseSerializer
from drf_yasg.utils import swagger_auto_schema
from .Services.user_services import UserService

user_service = UserService()


class SignUpView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        is_valid = user_service.check_user_validation(request.data)
        if not is_valid:
            return Response("회원가입에 실패하였습니다.", status=400)
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()  # DB 저장
            return Response(serializer.data, status=201)


class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=LoginRequestSerializer, response_body=LoginResponseSerializer)
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['user_id'] == "None":  # email required
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': True,
            'token': serializer.data['token'],  # 시리얼라이저에서 받은 토큰 전달
        }
        return Response(response, status=status.HTTP_200_OK)
