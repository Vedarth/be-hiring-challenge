# Generated by Django 3.0.2 on 2020-01-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='dataset')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
