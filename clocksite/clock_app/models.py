from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shifts():
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(default = 0)
    created_by = models.ForeignKey(User)
    