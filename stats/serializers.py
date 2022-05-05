from attr import field
from stats.models.models import UserInfo, Board, Records
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'comment', 'likes', 'create_datetime', 'create_user', 'delete_yn']


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'


class BoardRequestSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()


class BoardPostInnerBoardSerializer(serializers.Serializer):
    title = serializers.CharField()
    comment = serializers.CharField()
    likes = serializers.CharField()


class BoardPostPutInnerRecordSerializer(serializers.Serializer):
    duration = serializers.IntegerField()
    position = serializers.CharField()
    scores = serializers.IntegerField()
    rebounds = serializers.IntegerField()
    offensive_rebounds = serializers.IntegerField()
    assists = serializers.IntegerField()
    screen_assists = serializers.IntegerField()
    good_screens = serializers.IntegerField()
    blockshots = serializers.IntegerField()
    threepoints = serializers.IntegerField()
    hustle_plays = serializers.IntegerField()
    memo = serializers.CharField()


class BoardPostPutRequestSerializer(serializers.Serializer):
    board = BoardPostInnerBoardSerializer()
    records = BoardPostPutInnerRecordSerializer()
