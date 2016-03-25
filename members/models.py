from django.db import models

class Member(models.Model):
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return ("%s, %s '%s' %s" % (self.family_name, self.given_name, self.nickname, self.middle_name))