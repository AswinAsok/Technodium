from django.db import models


# Create your models here.


class Event(models.Model):
    #id is automatically generated for each Instance by django
    event_name = models.CharField(max_length=30, blank=False) 
    registration_fees = models.FloatField(blank=False) 
    #registration_fees = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')


    event_description = models.CharField(max_length=250)
    event_contact = models.CharField(max_length=15)
    event_start_time = models.DateField(blank=True, null=True)
    event_end_time = models.DateField(blank=True, null=True)

    event_iscompleted = models.BooleanField(default=False,blank=False)
    
    def __str__(self):
        return self.event_name
        


class Registration(models.Model):
    
    full_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank = False)
    institute_name = models.CharField(max_length=50)
    github_profile = models.CharField(max_length=50)

    event = models.ForeignKey(Event, on_delete = models.CASCADE,default="")


    def __str__(self):
        return self.full_name

    