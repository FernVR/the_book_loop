# Generated by Django 5.1.3 on 2024-12-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_alter_book_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
