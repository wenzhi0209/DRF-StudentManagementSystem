from unicodedata import name
from django.db import models
from apps.utils.models import Timestamps
# Create your models here.
class Certificate(Timestamps,models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()

    def __str__(self):
        return self.name
    
