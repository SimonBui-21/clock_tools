from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Shifts(models.Model):
    created_by = models.CharField(max_length=256)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)
    # created_by = models.ForeignKey(User)
    def __str__(self):
        return self.created_by
    
# class ShiftsList(models.Model):

