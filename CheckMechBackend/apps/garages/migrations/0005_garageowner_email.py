# Generated by Django 4.1.2 on 2022-11-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garages', '0004_rename_provider_service_garage'),
    ]

    operations = [
        migrations.AddField(
            model_name='garageowner',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]