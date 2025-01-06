# Generated by Django 5.1.1 on 2024-11-06 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_chatmessage_receiver'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
