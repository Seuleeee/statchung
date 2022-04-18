import django
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from stats.models import Board, Records
import datetime
import json
import pytest
from django.test import TestCase


class StatsApiTests(APITestCase):
    def setUp(self):
        datetime_now = datetime.datetime.now()
        board, _ = Board.objects.get_or_create(
            title='테스트 기록 제목',
            comment='테스트기록은 테스트코멘트지',
            likes='Y',
            create_user='test',
            create_datetime='datetime_now'
        )

        record, _ = Records.objects.get_or_create(
            board=board.pk,
            duration=40,
            position='SF',
            scores=24,
            rebounds=3,
            offensive_rebounds=1,
            assists=4,
            screen_assists=4,
            good_screens=5,
            blockshots=2,
            threepoints=1,
            hustle_plays=1,
            memo='blahblahblah'
        )
        self.create_read_url = reverse('api:stats:boards-list')
        self.read_update_delete_url = reverse('api:stats:boards-detail', kwargs={'pk': board.pk})

    def test_list(self):
        response = self.client.get(self.create_read_url)
        self.assertContains(response, '꿔버_test')
        self.assertContains(response, '꿔버_test2')
