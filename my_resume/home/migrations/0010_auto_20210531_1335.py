# Generated by Django 3.0.7 on 2021-05-31 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210527_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagehit',
            options={'verbose_name': 'счётчик', 'verbose_name_plural': 'счётчики'},
        ),
    ]
