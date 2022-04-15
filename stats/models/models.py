from django.db import models
from stats.models.base import TimeStampedModel
# Create your models here.


class UserInfo(TimeStampedModel):
    user_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=512)
    nickname = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=4)

    class Meta:
        db_table = 'USER'


class Board(TimeStampedModel):
    board_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    likes = models.CharField(max_length=1)

    class Meta:
        db_table = 'BOARD'


class Records(models.Model):
    board = models.ForeignKey(Board, related_name='board', on_delete=models.CASCADE, db_column='board_id')
    duration = models.IntegerField()
    position = models.CharField(max_length=2, blank=True)
    scores = models.IntegerField(blank=True)
    rebounds = models.IntegerField(blank=True)
    offensive_rebounds = models.IntegerField(blank=True)
    assists = models.IntegerField(blank=True)
    screen_assists = models.IntegerField(blank=True)
    good_screens = models.IntegerField(blank=True)
    blockshots = models.IntegerField(blank=True)
    threepoints = models.IntegerField(blank=True)
    hustle_plays = models.IntegerField(blank=True)
    memo = models.TextField(max_length=500, blank=True)

    class Meta:
        db_table = 'RECORDS'


class EditDashboard(models.Model):
    dashboard_id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'EDIT_DASHBOARD'


class EditDashboardOrder(models.Model):
    dashboard = models.ForeignKey(EditDashboard, related_name='dashboard',
                                  on_delete=models.CASCADE, db_column='dashboard_id')
    order = models.IntegerField()
    record_nm = models.CharField(max_length=10)

    class Meta:
        db_table = 'EDIT_DASHBOARD_ORDER'
