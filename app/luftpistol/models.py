from django.db import models
from django.utils import timezone

import uuid

class image(models.Model):
    image_namne = models.CharField(max_length=100, unique=True)
    image_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image_creation_time = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.image_creation_time