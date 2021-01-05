from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    

    class Meta:
        model = Registration
        fields = ('full_name','email', 'institute_name','github_profile','event')
