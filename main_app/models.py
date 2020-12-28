from django.db import models
from django.urls import reverse

METHODS = (
    ('T', 'Traditional'),
    ('SP', 'Sport'),
    ('TR', 'Top Rope'),
    ('S', 'Free Solo'),
    ('A', 'Aid Climbed'),
    ('B', 'Boulder')
)

INFOS = (
    ('RP', 'Redpoint'),
    ('PP', 'Pinkpoint'),
    ('OS', 'Onsight'),
    ('F', 'Flash'),
)


# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    crag = models.CharField(max_length=50)
    rock_type = models.CharField(max_length=50)
    pitches = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'route_id': self.id})

class Send(models.Model):
    date = models.DateField('Climbed On:')
    method = models.CharField(
        max_length=10,
        choices=METHODS,
        default=METHODS[0][0])
    info = models.CharField(
        max_length=10,
        choices=INFOS,
        default=INFOS[0][0])
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.method} {self.info} on {self.date}"