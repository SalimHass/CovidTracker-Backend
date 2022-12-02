from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from mainApp.models import MyCovidRecord
from mainApp.serializer import MyCovidRecordSerializer


class MyCovidRecordViewSet(viewsets.ModelViewSet):
    queryset = MyCovidRecord.objects.all()
    serializer_class = MyCovidRecordSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
