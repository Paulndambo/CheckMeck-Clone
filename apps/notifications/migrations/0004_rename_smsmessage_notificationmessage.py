# Generated by Django 4.1.2 on 2022-11-21 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_smsmessage_notification_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SmsMessage',
            new_name='NotificationMessage',
        ),
    ]