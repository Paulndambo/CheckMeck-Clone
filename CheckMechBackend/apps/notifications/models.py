from django.db import models

# Create your models here.
NOTIFICATION_TYPES = (
    ("sms", "SMS"),
    ("email", "Email"),
)

class NotificationMessage(models.Model):
    destination_address = models.CharField(max_length=255)  ##Customer Phone Number
    content = models.TextField() ## The Body of the message
    driver_phone_number = models.CharField(max_length=255)
    driver_location = models.JSONField(null=True)
    notification_type = models.CharField(max_length=255, choices=NOTIFICATION_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.destination_address