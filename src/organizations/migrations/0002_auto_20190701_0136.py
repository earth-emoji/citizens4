# Generated by Django 2.2.2 on 2019-07-01 01:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AddField(
            model_name='organizationrequest',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
    ]
