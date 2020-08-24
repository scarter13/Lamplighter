from django.db import models
from users.models import User

class Address(models.Model):
    pass

class Company(models.Model):
    name = models.CharField(max_length=255)
    address_one = models.CharField(max_length=255, blank=True, null=True)
    address_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)


class Contact(models.Model):
    BOOSTER = 'BOOSTER'
    OBLIGATE = 'OBLIGATE'
    CURMUDGEON = 'CURMUDGEON'
    NOT_RATED = 'NR'
    STATUS_CHOICES =[
        (BOOSTER, 'Booster'),
        (OBLIGATE, 'Obligate'),
        (CURMUDGEON, 'Curmudgeon'),
        (NOT_RATED, 'Not Yet Rated'),
    ]
    ALUMNI = 'ALUMNI'
    ADVOCATE = 'ADVOCATE'
    UNKNOWN = 'UNKNOWN'
    RELATIONSHIP_CHOICES =[
        (ALUMNI, 'Alumni'),
        (ADVOCATE, 'Advocate'),
        (UNKNOWN, 'Not Known'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default=NOT_RATED)
    relationship = models.CharField(max_length=8, choices=RELATIONSHIP_CHOICES, default=UNKNOWN)

    #first_contact = models.DateField(blank=True, null=True)

class CallDate(models.Model):
    pass
    




