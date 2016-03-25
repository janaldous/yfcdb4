from django.db import models

class Member(models.Model):
    #names
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True)
    #address
    address_st = models.CharField(max_length=200)
    address_village = models.CharField(max_length=200)
    address_city = models.CharField(max_length=200)
    #birthday
    birthday = models.DateField(blank=True)
    #kfc to yfc
    kfc_to_yfc = models.BooleanField(default=False)


    def __str__(self):
        return ("%s, %s '%s' %s" % (self.family_name, self.given_name, self.nickname, self.middle_name))