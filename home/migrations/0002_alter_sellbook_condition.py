# Generated by Django 5.1.3 on 2025-01-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellbook',
            name='condition',
            field=models.CharField(blank=True, choices=[('like-new', 'Like New'), ('good', 'Good'), ('fair', 'Fair')], max_length=10, null=True),
        ),
    ]
