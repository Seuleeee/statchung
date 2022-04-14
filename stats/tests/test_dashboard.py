from rest_framework import status
from rest_framework.test import APITestCase
from stats.models.models import Stats
import json


class DashBoardApiTest(APITestCase):
    def setUp(self):
        for num in range(10):
            stat_one, _ = Stats.objects.get_or_create(
                scores=24,
                rebounds=9,
                offensive_rebounds=5,
                assists=num,
                screen_assists=5,
                good_screens=3,
                blockshots=10,
                threepoints=3,
                hustle_plays=5,
                memo='꿔버테스트테스트테스트',
                create_datetime="2022-04-07T08:43:19.614000Z",
                create_user='hsjo'
            )

        self.dashboard_url_prefix = '/api/v1/dashboard/'

    def test_get_dashboard_stats(self):
        response = self.client.get('/api/v1/dashboard/assists')
        response_content = json.loads(response.content)
        for idx, assist in enumerate(response_content):
            self.assertEquals(assist, idx)
