# Generated by Django 3.1.6 on 2021-04-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_auto_20210429_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
