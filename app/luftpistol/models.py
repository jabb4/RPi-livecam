from django.db import models
from django.utils  import timezone
from zoneinfo import ZoneInfo

import uuid

class image(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    creation_time = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.creation_time.astimezone(ZoneInfo("Europe/Stockholm")).strftime("%d/%m/%Y %H:%M:%S"))
    
class saved_images(models.Model):
    name = models.CharField(max_length=100, unique=True)
    count = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)