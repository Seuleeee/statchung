from stats.models.models import UserInfo
from rest_framework.response import Response
import re
import bcrypt


class UserService:
    def set_account(self, request):
        user_id = request['user_id']
        password = request['password']
        nickname = request['nickname']
        email = request['e-mail']
        phone = request['phone']

        is_user_id_validate = self.__check_user_id_validation(user_id)
        is_password_validate = self.__check_password_validation(password)
        is_email_validate = self.__check_email_validation(email)
        is_phone_validate = self.__check_phone_validate(phone)
        is_nickname_validate = self.__check_nickname_validate(nickname)

        if is_user_id_validate['status'] == 400:
            return is_user_id_validate
        if is_password_validate['status'] == 400:
            return is_password_validate
        if is_email_validate['status'] == 400:
            return is_email_validate
        if is_phone_validate['status'] == 400:
            return is_phone_validate
        if is_nickname_validate['status'] == 400:
            return is_nickname_validate

        hashed_password = self.__generate_hashed_password(password)

        try:
            UserInfo.objects.create(
                user_id=user_id,
                password=hashed_password,
                nickname=nickname,
                phone=phone,
                email=email,
                status=1
            )
            return {
                "message": "SUCCESS",
                "status": 201
            }
        except:
            return {
                "message": "회원가입에 실패하였습니다.",
                "status": 400
            }

    def __generate_hashed_password(self, password: str):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        decoded_password = hashed_password.decode('utf-8')
        return decoded_password

    def __check_user_id_validation(self, user_id: str) -> bool:
        if UserInfo.objects.filter(user_id=user_id).exists():
            return {
                "message": "이미 존재하는 아이디 입니다.",
                "status": 400
            }
        regex_user_id = r'^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$'
        if re.match(regex_user_id, user_id):
            return {
                "message": "SUCCESS",
                "status": 200
            }
        else:
            return {
                "message": "아이디는 8~20 자의 영문, 숫자로 만들어주세요.",
                "status": 400
            }

    def __check_password_validation(self, password: str) -> bool:
        reg_password = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,20}$'
        if re.match(reg_password, password):
            return {
                "message": "SUCCESS",
                "status": 200
            }
        else:
            return {
                "message": "비밀번호는 8~20 자의 영문, 숫자, 특수문자를 조합해 만들어주세요.",
                "status": 400
            }

    def __check_email_validation(self, email: str) -> bool:
        if UserInfo.objects.filter(email=email).exists():
            return {
                "message": "이미 존재하는 e-mail 입니다.",
                "status": 400
            }
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(regex_email, email):
            return {
                "message": "SUCCESS",
                "status": 200
            }
        else:
            return {
                "message": "올바른 email 형식을 입력해 주세요. ex) test@test.com",
                "status": 400
            }

    def __check_phone_validate(self, phone: str) -> bool:
        reg_phone = r'^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$'
        if re.match(reg_phone, phone):
            return {
                "message": "SUCCESS",
                "status": 200
            }
        else:
            return {
                "message": "올바른 휴대전화 번호 양식을 입력해 주세요. ex) 010-1234-1234",
                "status": 400
            }

    def __check_nickname_validate(self, nickname: str) -> bool:
        if UserInfo.objects.filter(nickname=nickname).exists():
            return {
                "message": "이미 존재하는 닉네임 입니다.",
                "status": 400
            }
        regex_nickname = r'^(?=[가-힣a-zA-Z0-9._]{4,20}$)(?!.*[_.]{2})[^_.].*[^_.]$'
        if re.match(regex_nickname, nickname):
            return {
                "message": "SUCCESS",
                "status": 200
            }
        else:
            return {
                "message": "닉네임은 8~20 자의 문자, 숫자로 만들어주세요.",
                "status": 400
            }
