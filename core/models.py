from django.db import models

class Address(models.Model):
    pass

class Company(models.Model):
    name = models.CharField(max_length=255)
    address_one = models.Charfield(max_length=255, blank=true, null=true)
    address_two = models.Charfield(max_length=255, blank=true, null=true)
    city = models.Charfield(max_length=255, blank=true, null=true)
    state = models.Charfield(max_length=255, blank=true, null=true)
    zip_code = models.Charfield(max_length=255, blank=true, null=true)
    email = models.EmailField(max_length=255, blank=true, null=true)


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
    phone = models.Charfield(max_length=14, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default=NOT_RATED)
    relationship = models.CharField(max_length=8, choices=RELATIONSHIP_CHOICES, default=UNKNOWN)
    
    #first_contact = models.DateField(blank=True, null=True)

class CallDate(models.model):
    pass
    




