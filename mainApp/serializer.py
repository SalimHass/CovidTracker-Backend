from rest_framework import serializers
from mainApp.models import MyCovidRecord


class MyCovidRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCovidRecord
        fields = '__all__'

