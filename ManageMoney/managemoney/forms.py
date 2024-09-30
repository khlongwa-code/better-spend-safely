from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
            'class': 'form-control'
            }
        )
    )


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'form-control'
            }
        ) 
    )

    last_name = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'form-control'
            }
        ) 
    )

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
            'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
            'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_admin', 'is_client')