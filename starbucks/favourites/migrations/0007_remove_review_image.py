# Generated by Django 4.1.7 on 2023-03-20 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0006_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
    ]
