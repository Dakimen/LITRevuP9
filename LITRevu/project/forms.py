from django import forms


class ConnectForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput())
    password_2 = forms.CharField(label='Confirmer mot de passe', widget=forms.PasswordInput())
