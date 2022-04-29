from stats.models.models import UserInfo
import re
from ..exceptions import InvalidUserIDException, InvalidPasswordException, InvalidNickNameException, DuplicateNicknameException
from ..consts import REG_NICKNAME, REG_USER_ID, REG_PASSWORD, REG_PHONE


class UserService:
    def check_user_validation(self, request):
        user_id = request['user_id']
        password = request['password']
        nickname = request['nickname']

        is_user_id_validate = self.__check_user_id_validation(user_id)
        is_password_validate = self.__check_password_validation(password)
        is_nickname_validate = self.__check_nickname_validate(nickname)

        if is_user_id_validate and is_password_validate and is_nickname_validate:
            return True
        return False

    def __check_user_id_validation(self, user_id: str) -> bool:
        regex_user_id = REG_USER_ID
        if re.match(regex_user_id, user_id):
            return True
        else:
            raise InvalidUserIDException()

    def __check_password_validation(self, password: str) -> bool:
        reg_password = REG_PASSWORD

        if re.match(reg_password, password):
            return True
        else:
            raise InvalidPasswordException()

    def __check_nickname_validate(self, nickname: str) -> bool:
        if UserInfo.objects.filter(nickname=nickname).exists():
            raise DuplicateNicknameException()
        regex_nickname = REG_NICKNAME
        if re.match(regex_nickname, nickname):
            return True
        else:
            raise InvalidNickNameException()
