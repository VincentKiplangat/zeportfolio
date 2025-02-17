from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=False)
    class Meta:
        model = Contact
        fields = '__all__'