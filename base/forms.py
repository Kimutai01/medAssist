from django import forms
from .models import UserFormSubmission

class WaitlistForm(forms.ModelForm):
    class Meta:
        model = UserFormSubmission
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'profession')