# Generated by Django 5.1.3 on 2025-01-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersupport',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customersupport',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customersupport',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
