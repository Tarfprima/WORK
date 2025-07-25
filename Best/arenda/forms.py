from django import forms
from . import models
from django.contrib.auth.models import User

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.Arenda
        fields = [
            'title',
            'text'
        ]

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username', 
            'email'
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(
                "Passwords don't match.")
        return cd['password2']