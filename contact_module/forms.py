from django import forms
from .models import ContactUsModel


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['full_name', 'email', 'title', 'text']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea()
        }

        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری است. لطفا وارد نمایید'
            }
        }
