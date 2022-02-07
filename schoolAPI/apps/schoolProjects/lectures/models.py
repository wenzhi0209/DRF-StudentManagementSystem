from django.db import models
from django.forms import CharField
from apps.utils.models import Timestamps
# Create your models here.


class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    lecturer_name=models.CharField(max_length=100,blank=True)
    date = models.DateField()
    slides_url = models.CharField(max_length=255)
    duration=models.IntegerField(help_text='Enter number of hours', default=1)
    is_required=models.BooleanField(default=True)
