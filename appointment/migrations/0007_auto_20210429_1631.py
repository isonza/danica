# Generated by Django 3.1.6 on 2021-04-29 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_auto_20210429_1209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='User',
        ),
    ]