from django import forms
from contact.models import ContactLead


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactLead
        fields = ('first_name', 'last_name', 'email', 'message')