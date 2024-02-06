from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(default=0),
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ph_no = models.IntegerField(default=0)
    Blood_Group = models.CharField(max_length=30)
