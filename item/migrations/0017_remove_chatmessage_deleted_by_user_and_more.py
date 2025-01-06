# Generated by Django 5.1.1 on 2024-11-09 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0016_chatmessage_deleted_by_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='deleted_by_user',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='deleted_by_user',
            field=models.ManyToManyField(blank=True, related_name='deleted_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
