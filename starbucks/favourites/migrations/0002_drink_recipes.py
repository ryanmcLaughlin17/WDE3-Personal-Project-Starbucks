# Generated by Django 4.1.7 on 2023-03-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='recipes',
            field=models.TextField(max_length=100, null=True),
        ),
    ]