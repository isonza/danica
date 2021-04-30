# Generated by Django 3.1.6 on 2021-04-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20210428_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='address',
        ),
        migrations.RemoveField(
            model_name='item',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='item',
            name='email',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='contactnumber',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='emailaddress',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='fulladdress',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]