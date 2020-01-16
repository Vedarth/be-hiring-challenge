from rest_framework.serializers import ModelSerializer, SerializerMethodField
from dataset.models import FileList
from os.path import basename

class DataSetSerializer(ModelSerializer):
    name = SerializerMethodField('csv_name')
    size = SerializerMethodField('csv_size')
    class Meta:
        model = FileList
        fields = ['id', 'file_reference', 'timestamp', 'name', 'size']

    def csv_name(self, path):
        return basename(path.file_name.name)

    def csv_size(self, path):
        return path.file_name.size