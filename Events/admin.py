from django.contrib import admin
from .models import Event, Registration

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_description', 'registration_fees', 'event_iscompleted')
    search_fields = ('event_name','registration_fees')

    

    class Meta:
        model = Event


admin.site.register(Event,EventAdmin)
admin.site.register(Registration)
