# Generated by Django 3.2.2 on 2021-05-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210509_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Имя проекта',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
