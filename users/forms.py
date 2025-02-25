from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, EmailField, EmailInput, CharField, PasswordInput, TextInput

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control email',
                'placeholder': 'Імя користувача',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control email',
                'placeholder': 'Ваша пошта',
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте пароль',
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторіть пароль'
            })
        }

class EmailPasswordForm(Form):
    email = EmailField(
        label="Електронна пошта", 
        widget=EmailInput(attrs={
            'class': 'form-control email',
            'placeholder': 'Ваша пошта',
        })
    )
    password = CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control email',
            'placeholder': 'Пароль',
        }),
        label="Пароль"
    )