from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    crag = models.CharField(max_length=50)
    rock_type = models.CharField(max_length=50)
    pitches = models.IntegerField()
    