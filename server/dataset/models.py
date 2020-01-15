from django.db import models

# Create your models here.

class FileList(models.Model):
    file_name = models.FileField(upload_to='dataset')
    timestamp = models.DateTimeField(auto_now_add=True)