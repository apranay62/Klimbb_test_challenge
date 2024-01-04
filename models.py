from django.db import models
import uuid

# Create your models here.


class Incident(models.Model):
    incident_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=255)
    severity = models.IntegerField()
    timestamp = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=255)
    assigned_to = models.CharField(max_length=255, blank=True)
