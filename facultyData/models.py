from django.db import models

# Create your models here.


class Faculty(models.Model):
    fName = models.CharField(max_length=10)
    fDept = models.CharField(max_length=10)
    fSal = models.IntegerField()
