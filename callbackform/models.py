from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

STATUS_CHOICES = [
    ('o', 'Outstanding'),
    ('a', 'Archived'),
]

class Callback (models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=70, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    problem_description = models.CharField(max_length=1000)
    submitted_date_time = models.DateTimeField()
    support_date_time = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Not reviewed')

    def __str__(self):
        return self.subject

# class Archieved (models.Model):
#     callbackform = models.ForeignKey(CallbackForm, on_delete=PROTECT)