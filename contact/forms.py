from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone", "message")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Name"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email Adress"
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone Number"
                }
            ),
            "message": forms.TextInput(
                attrs={
                    "placeholder": "Your message"
                }
            ),
        }