from re import T
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Stats(models.Model):
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
    create_datetime = models.DateTimeField(auto_created=True)
    update_datetime = models.DateTimeField(null=True)
    create_user = models.CharField(max_length=20)
    update_user = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'STATS'
