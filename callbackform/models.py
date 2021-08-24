from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('o', 'Outstanding'),
    ('a', 'Archived'),
]

class CallbackForm (models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=70, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    problem_descritpion = models.CharField(max_length=1000)
    submitted_date_time = models.DateTimeField(auto_now=True)
    support_date_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Not reviewed')

    def __str__(self):
        return self.subject
