from django.db import models
from users.models import User
from phone_field import PhoneField


class Company(models.Model):
    UNDECIDED = 'UNDECIDED'
    MILD = 'MILD'
    MODERATE = 'MODERATE'
    HIGH = 'HIGH'
    MOTIVATION_CHOICES =[
        (UNDECIDED, 'Undecided'),
        (MILD, 'Mild'),
        (MODERATE, 'Moderate'),
        (HIGH, 'High'),
        ]
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="companies")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    motivation = models.CharField(max_length=9, choices=MOTIVATION_CHOICES, default=UNDECIDED)
    careers = models.URLField(null=True, blank=True, help_text='(A link to the company job board)')

    def __str__(self):
        return self.name

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
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneField(blank=True, null=True, help_text='Contact Phone Number')
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default=NOT_RATED)
    relationship = models.CharField(max_length=8, choices=RELATIONSHIP_CHOICES, default=UNKNOWN)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, blank=True, null=True, related_name="contacts")

    #first_contact = models.DateField(blank=True, null=True)

class Conversation(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="conversations")
    contact = models.ForeignKey(to=Contact, on_delete=models.CASCADE, null=True, related_name="conversations")
    title = models.CharField(max_length=255, blank=True, null=True, default="Untitled")
    notes = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True) 


    class Meta:
        ordering = ['-pk']

class CompanyNote(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="company_notes")
    title = models.CharField(max_length=255, blank=True, null=True, default="Untitled")
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, null = True, related_name = "notes")
    text = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

class ContactNote(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="contact_notes")
    contact = models.ForeignKey(to=Contact, on_delete=models.CASCADE, null = True, related_name = "notes")
    title = models.CharField(max_length=255, blank=True, null=True, default="Untitled")
    text = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

