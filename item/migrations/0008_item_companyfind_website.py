# Generated by Django 5.1.1 on 2024-10-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_alter_item_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='companyfind_website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
