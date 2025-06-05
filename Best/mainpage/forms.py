from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    """
    Оболочка над User, чтобы ввести username, email, password и password2.
    Проверяем, что пароли совпадают в clean_password2.
    """
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Будущий логин',
            'email': 'Электронная почта'
        }
        help_texts = {
            'username': None  # убираем подсказку «Обязательное поле» или шаблон Django
        }

    def clean_password2(self):
        """
        Убеждаемся, что два поля с паролями совпадают.
        Если нет — вызываем ValidationError.
        """
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError("Пароли не совпадают.")
        return cd.get('password2')
