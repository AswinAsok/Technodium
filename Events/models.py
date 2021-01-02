from django.db import models

# Create your models here.

class Event(models.Model):
    #id is automatically generated for each Instance by django
    event_name = models.CharField(max_length=30, blank=False) 
    registration_fees = models.FloatField(blank=False) 
    event_categories = models.CharField(max_length=100)
    event_description = models.CharField(max_length=250)
    event_contact = models.CharField(max_length=15)
    event_start_time = models.DateField(blank=True, null=True)
    event_end_time = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.event_name