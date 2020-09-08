from django.db import models
from users.models import User

class Address(models.Model):
    pass

class Company(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="companies")
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
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="contacts")
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default=NOT_RATED)
    relationship = models.CharField(max_length=8, choices=RELATIONSHIP_CHOICES, default=UNKNOWN)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, blank=True, null=True, related_name="contacts")

    #first_contact = models.DateField(blank=True, null=True)

class Conversation(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="conversations")
    contact = models.ForeignKey(to=Contact, on_delete=models.CASCADE, null=True, related_name="conversations")
    date = models.DateTimeField(auto_now_add=True) 
    follow_up_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    