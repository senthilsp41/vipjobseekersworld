# Generated by Django 5.1.1 on 2024-10-05 12:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Category'},
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('company_description', models.TextField(blank=True, null=True)),
                ('job_title', models.CharField(max_length=255)),
                ('job_location', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('internship', 'Internship'), ('contract', 'Contract')], max_length=50)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('interview_date', models.DateField()),
                ('interview_rounds', models.TextField()),
                ('interview_type', models.CharField(choices=[('walkin', 'Walk-in'), ('reference', 'Reference'), ('online', 'Online'), ('phone', 'Phone')], max_length=50)),
                ('interview_feedback', models.TextField(blank=True, null=True)),
                ('candidate_name', models.CharField(max_length=255)),
                ('candidate_email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=False)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
