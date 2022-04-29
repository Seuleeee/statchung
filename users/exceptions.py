from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidUserIDException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '''아이디는 8~20 자의 영문, 숫자로 만들어주세요.'''


class DuplicateNicknameException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '''이미 사용 중인 닉네임 입니다.'''


class InvalidNickNameException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '''닉네임은 4~20 자의 문자, 숫자로 만들어주세요.'''


class InvalidPasswordException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '''비밀번호는 8~20 자의 영문, 숫자, 특수문자를 조합해 만들어주세요.'''
