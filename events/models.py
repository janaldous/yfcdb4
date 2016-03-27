from django.db import models
from members.models import Member
from django.core.urlresolvers import reverse

EVENT_TYPE = (
    ("CA", "Chapter Assembly"),
    ("PF", "Pastoral Formation"),
    ("YC", "Youth Camp"),
    ("HH", "Household"),
    ("Cf", "Conference"),
    ("Ka", "Kassanga"),
    ("SM", "Service Meeting"),
)

ROLE = (
    ('P', 'Present'),
    ('Spk', 'Speaker'),
    ('Shr', 'Sharer'),
    ('Hhl', 'Household Leader'),
    ('ST', 'Service Team'),
    ('TL', 'Team Leader'),
    ('ATL', 'Assistant Team Leader'),
    ('HS', 'Head Servant'),
    ('AHS', 'Assistant Head Servant'),
    ('PW', 'Prayer Warrior'),
    ('FC', 'Food Committee'),
    ('MM', 'Music Ministry'),
)

class Event(models.Model):
    #names
    date = models.DateField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=EVENT_TYPE)
    venue = models.CharField(max_length=50)
    attendees = models.ManyToManyField(
        Member,
        through='Attend',
        through_fields=('event', 'member'),
    )

    def __str__(self):
        return ("%s: %s at %s" % (self.date, self.name, self.venue))

    def get_absolute_url(self):
        return reverse('events:event_index')

class Attend(models.Model):
    #names
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=ROLE)

    def __str__(self):
        return ("%s %s attended %s" % (self.member.nickname, self.member.family_name, self.event.name))