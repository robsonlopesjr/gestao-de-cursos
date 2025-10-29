from django import forms

from .models import ConctactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ConctactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite seu nome",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite seu e-mail",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o assunto",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a sua mensagem",
                }
            ),
        }
