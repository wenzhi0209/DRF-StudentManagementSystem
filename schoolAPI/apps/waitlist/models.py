import email
from errno import EMLINK
from unicodedata import name
from django.db import models

from apps.users.models import User
from apps.utils.models import Timestamps
# Create your models here.


class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )
    level=models.IntegerField(verbose_name='Class Level',default=1)
    notes = models.TextField()
    user_id=models.ForeignKey(
        User,
        blank=True, 
        null=True,
        on_delete=models.DO_NOTHING,
    )


    class Meta:
        verbose_name_plural= 'Waitlist Entries'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    
