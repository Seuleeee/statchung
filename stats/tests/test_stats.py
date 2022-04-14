from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from stats.models.models import Stats
import datetime
import json


class StatsApiTests(APITestCase):
    def setUp(self):
        datetime_now = datetime.datetime.now()
        stat_one, _ = Stats.objects.get_or_create(
            scores=24,
            rebounds=9,
            offensive_rebounds=5,
            assists=15,
            screen_assists=5,
            good_screens=3,
            blockshots=10,
            threepoints=3,
            hustle_plays=5,
            memo='꿔버테스트테스트테스트',
            create_datetime=datetime_now,
            create_user='꿔버_test'
        )
        stat_two, _ = Stats.objects.get_or_create(
            scores=241,
            rebounds=92,
            offensive_rebounds=15,
            assists=1,
            screen_assists=5,
            good_screens=3,
            blockshots=10,
            threepoints=3,
            hustle_plays=5,
            memo='꿔버테스트테스트테스트',
            create_datetime=datetime_now,
            create_user='꿔버_test2'
        )
        self.create_read_url = reverse('api:stats:stats-list')
        self.read_update_delete_url = reverse('api:stats:stats-detail', kwargs={'pk': stat_one.pk})

    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertContains(response, '꿔버_test')
        self.assertContains(response, '꿔버_test2')

    def test_detail(self):
        response = self.client.get(self.read_update_delete_url)
        data = json.loads(response.content)
        create_user = '꿔버_test'
        self.assertEqual(data['create_user'], create_user)

    def test_create(self):
        datetime_now = datetime.datetime.now()
        post = {
            'scores': 16,
            'rebounds': 2,
            'offensive_rebounds': 0,
            'assists': 1,
            'screen_assists': 2,
            'good_screens': 1,
            'blockshots': 0,
            'threepoints': 0,
            'hustle_plays': 5,
            'memo': '꿔버테스트테스트테스트',
            'create_datetime': datetime_now,
            'create_user': '꿔버_test3'
        }
        response = self.client.post(self.create_read_url, post)
        data = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        content = {
            'scores': 16,
            'rebounds': 2,
            'offensive_rebounds': 0,
            'assists': 1,
            'screen_assists': 2,
            'good_screens': 1,
            'blockshots': 0,
            'threepoints': 0,
            'hustle_plays': 5,
            'memo': '꿔버테스트테스트테스트',
            'create_datetime': datetime_now,
            'create_user': '꿔버_test3'
        }

        # self.assertEquals(data, content)
        self.assertEquals(Stats.objects.count(), 3)

    def test_delete(self):
        response = self.client.delete(self.read_update_delete_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Stats.objects.count(), 1)
