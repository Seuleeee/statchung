from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidUserRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '''해당 유저의 최근 기록이 없습니다.'''
