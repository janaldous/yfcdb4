from django.db import models
from members.models import Member

EVENT_TYPE = (
    ("PF", "Pastoral Formation"),
)

ROLE = (
    ('P', 'Present'),
    ('Spk', 'Speaker')
)

class Event(models.Model):
    #names
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=EVENT_TYPE)
    venue = models.CharField(max_length=50)

    def __str__(self):
        return ("%s: %s at %s" % (self.date, self.name, self.venue))

class Attend(models.Model):
    #names
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=ROLE)

    def __str__(self):
        return ("%s %s attended %s" % (self.member.nickname, self.member.family_name, self.event.name))