from django.db import models
from django.contrib.auth.models import User
from stats.models.base import TimeStampedModel
# Create your models here.


class Users(TimeStampedModel):
    user_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=512)
    user_nm = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'Users'


class Stats(TimeStampedModel):
    stat_id = models.AutoField(primary_key=True)
    scores = models.IntegerField(null=True)
    rebounds = models.IntegerField(null=True)
    offensive_rebounds = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    screen_assists = models.IntegerField(null=True)
    good_screens = models.IntegerField(null=True)
    blockshots = models.IntegerField(null=True)
    threepoints = models.IntegerField(null=True)
    hustle_plays = models.IntegerField(null=True)
    memo = models.TextField(max_length=500, null=True)

    class Meta:
        db_table = 'STATS'
