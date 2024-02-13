from django.db import models

# Create your models here.
class Department(models.Model):
    deptname= models.CharField(max_length=200)


class students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ph_no = models.IntegerField(default=0)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,default=None)

