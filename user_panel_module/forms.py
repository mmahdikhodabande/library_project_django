from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'about_user', 'avatar']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),

            'avatar': forms.FileInput(),
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
            'address': 'آدرس'
        }

        #
        # error_messages = {
        #     'full_name': {
        #         'required': 'نام و نام خانوادگی اجباری است. لطفا وارد نمایید'
        #     }
        # }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))

    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
