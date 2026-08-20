from django.db import models
from django.utils import timezone


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"