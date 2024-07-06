from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=255)
    line=models.CharField(max_length=255)

class Part(models.Model):
    name=models.CharField(max_length=255)
    reference=models.CharField(max_length=255)
    
class displacement(models.Model):
    displacement = models.IntegerField()
    reference=models.CharField(max_length=255)
    
class manufacturer(models.Model):
    name=models.CharField(max_length=255)
    