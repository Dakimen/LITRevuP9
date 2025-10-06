"""
Forms module of the authentification app.
Contains:
CustomAuthenticationForm(AuthenticationForm) - used for User Authentication, containing:
    A character field for username
    A password field
SignUpForm(UserCreationForm) - form used to create a new account, containing:
    username - character field
    password1 - password field
    password2 - password confirmation
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomAuthenticationForm(AuthenticationForm):
    """CustomAuthenticationForm(AuthenticationForm) - used for User Authentication, containing:
    A character field for username
    A password field
    """
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password'
        })
    )


class SignUpForm(UserCreationForm):
    """SignUpForm(UserCreationForm) - form used to create a new account, containing:
    username - character field
    password1 - password field
    password2 - password confirmation
    """
    class Meta(UserCreationForm.Meta):
        """SignUpForm specifications, determining model to use and fields to display"""
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
