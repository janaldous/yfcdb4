from django.db import models

EVENT_TYPE = (
    ("PF", "Pastoral Formation"),
)

# Create your models here.
class Event(models.Model):
    #names
    date = models.DateField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=EVENT_TYPE)
    venue = models.CharField(max_length=50)

    def __str__(self):
        return ("%s: %s at %s" % (self.date, self.name, self.venue))