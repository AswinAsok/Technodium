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
    
    event_category = models.CharField(max_length=35,default="others", choices=(
        ('Web Development', 'Web Development'),
        ('App Development', 'App Development'),
        ('Others', 'Others'),
    ))
    
    def get_events(self):
        total_event = Event.objects.all().count()
        event_names = ()
        for event in range(total_event):
            name = (Event.objects.get(id=event+1).event_name,)
            name = name + (Event.objects.get(id=event+1).event_name,)
            event_names = event_names+ (name,)

        return(event_names)    

    def __str__(self):
        return self.event_name
        


class Registration(models.Model):
    
    full_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank = False)
    institute_name = models.CharField(max_length=50)
    github_profile = models.CharField(max_length=50)
    

    event = models.CharField(max_length=25,choices=Event.get_events(self=None), default="Select a Option")

    def __str__(self):
        return self.full_name

    