# Generated by Django 4.1.2 on 2022-11-17 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garages', '0003_remove_garage_user_alter_garage_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='provider',
            new_name='garage',
        ),
    ]
