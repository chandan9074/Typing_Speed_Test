from rest_framework import serializers

from .models import Quotes, Records


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = "__all__"


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = "__all__"
        extra_kwargs = {'easy': {'required': False}, 'userProfile': {'required': False},'medium': {'required': False}, 'hard': {'required': False}}