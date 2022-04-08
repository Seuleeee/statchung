import pytest
import datetime
from stats.models import Stats


@pytest.mark.django_db
def test_create_stats():
    datetime_now = datetime.datetime.now()
    stats = Stats.objects.create(
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
        create_user='꿔버_test')
    assert stats.scores == 24 and stats.create_user == '꿔버_test' and stats.memo == '꿔버테스트테스트테스트'
