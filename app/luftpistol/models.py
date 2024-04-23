from django.db import models
from django.utils import timezone

import uuid

class image(models.Model):
    namne = models.CharField(max_length=100, unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    creation_time = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.image_creation_time
    
class saved_images(models.Model):
    name = models.CharField(max_length=100, default="default")
    count = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.image_creation_time