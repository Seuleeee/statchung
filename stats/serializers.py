from stats.models.models import UserInfo
from rest_framework import serializers


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
