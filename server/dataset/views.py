from django.shortcuts import render
from rest_framework import viewsets
from dataset.models import FileList
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action
from dataset.serializers import DataSetSerializer
import pandas as pd

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = FileList.objects.all()
    serializer_class = DataSetSerializer
    