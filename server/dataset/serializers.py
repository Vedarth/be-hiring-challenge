from rest_framework.serializers import ModelSerializer
from dataset.models import FileList

class DataSetSerializer(ModelSerializer):
    class Meta:
        model = FileList
        fields = ['file_name', 'timestamp']
