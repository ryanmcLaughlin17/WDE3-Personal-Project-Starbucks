# Generated by Django 4.1.7 on 2023-03-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_rename_years_of_service_partner_partner_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='coffee_master',
            field=models.BooleanField(default=False),
        ),
    ]