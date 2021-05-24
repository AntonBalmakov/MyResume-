from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(initial='Your name')
    message_hr = forms.CharField(initial='Your message')

    class Meta:
        model = Contact
        fields ='__all__'