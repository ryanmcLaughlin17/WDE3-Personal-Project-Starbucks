# Generated by Django 4.1.7 on 2023-03-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_manager_fact'),
    ]

    operations = [
        migrations.AddField(
            model_name='barista',
            name='fact',
            field=models.TextField(max_length=250, null=True),
        ),
    ]