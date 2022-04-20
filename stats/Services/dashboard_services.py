from venv import create
from stats.models.models import UserInfo, Board
from datetime import date, timedelta


class DashboardService:
    def get_dashboard_recent(self, user_id: str):
        nickname = self.get_user_nickname(user_id)['nickname']
        user_level = self.get_user_level(user_id)
        return nickname+'님은 '+user_level+'입니다.'

    def get_user_nickname(self, user_id: str) -> str:
        nickname = UserInfo.objects.values('nickname').get(user_id=user_id)
        return nickname

    def get_user_level(self, user_id: str) -> str:
        date_format = '%y-%m-%d'
        now = date.today()
        before_one_week = now - timedelta(weeks=1)
        plays_per_week = Board.objects.filter(create_user=user_id, create_datetime__range=[
                                              before_one_week, now]).count()
        user_level = '농구초짜'
        if plays_per_week > 5:
            user_level = '농창인생'
        return user_level
