# Generated by Django 4.2.4 on 2023-10-03 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_reviews_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='watchAgain',
        ),
    ]
