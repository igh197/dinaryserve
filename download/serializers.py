from rest_framework import serializers
from .models import DownLoad


class DownLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownLoad  # product 모델 사용
        fields = '__all__'
