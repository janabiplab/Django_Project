from django.db import models

class member(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
