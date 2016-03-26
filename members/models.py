from django.db import models

BLOOD_TYPE = (
    ('B+', 'B+'),
)

GENDER = (
    ('m', 'Male'),
    ('f', 'Female'),
)

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
    #other
    kfc_to_yfc = models.BooleanField(default=False)
    school = models.CharField(max_length=100)
    school_level = models.CharField(max_length=10)
    course = models.CharField(max_length=100, blank=True)
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    cell_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    #parents
    name_of_father = models.CharField(max_length=100)
    fathers_occupation = models.CharField("Father's occupation", max_length=100, blank=True)
    fathers_contact_details = models.CharField("Father's cell #", max_length=100, blank=True)
    name_of_mother = models.CharField(max_length=100)
    mothers_occupation = models.CharField("Mother's occupation", max_length=100, blank=True)
    mothers_contact_details = models.CharField("Mother's cell #", max_length=100, blank=True)
    #other
    special_skills = models.CharField(
        max_length=100, blank=True,
        help_text="(eg playing musical instruments, dancing, singing, etc)",
    )
    illness = models.CharField(
        max_length=100, blank=True,
        help_text="Illnesses that require special attention",
    )

    def __str__(self):
        return ("%s, %s '%s' %s" % (self.family_name, self.given_name, self.nickname, self.middle_name))