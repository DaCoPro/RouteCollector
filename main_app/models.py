from django.db import models

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

GRADES = (
    ('< 5.4', '< 5.4'),
    ('5.4', '5.4'),
    ('5.5', '5.5'),
    ('5.6', '5.6'),
    ('5.7', '5.7'),
    ('5.8', '5.8'),
    ('5.9', '5.9'),
    ('5.10a', '5.10a'),
    ('5.10b', '5.10b'),
    ('5.10c', '5.10c'),
    ('5.10d', '5.10d'),
    ('5.11a', '5.11a'),
    ('5.11b', '5.11b'),
    ('5.11c', '5.11c'),
    ('5.11d', '5.11d'),
    ('5.12a', '5.12a'),
    ('5.12b', '5.12b'),
    ('5.12c', '5.12c'),
    ('5.12d', '5.12d'),
    ('5.13a', '5.13a'),
    ('5.13b', '5.13b'),
    ('5.13c', '5.13c'),
    ('5.13d', '5.13d'),
)

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(
        max_length=10,
        choices=GRADES)
    description = models.CharField(max_length=500)
    crag = models.CharField(max_length=50)
    rock_type = models.CharField(max_length=50)
    pitches = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.grade}"

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
    
    

