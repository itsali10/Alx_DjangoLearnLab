from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='notifications')
    actor=models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='actions')
    verb = models.CharField(max_length=255)
    target = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)