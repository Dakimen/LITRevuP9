from django.shortcuts import render, redirect
from authentification.forms import SignUpForm, CustomAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse


class CustomLoginView(LoginView):
    template_name = 'authentification/landing.html'
    redirect_authenticated_user = True
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse('flux')


def sign_up(request):
    if request.method == 'POST':
        register = SignUpForm(request.POST)
        if register.is_valid():
            user = register.save()
            login(request, user)
            return redirect('flux')
    else:
        register = SignUpForm()
        return render(request,
                      'authentification/sign_up.html',
                      {'form': register})
    

def logout_user(request):
    logout(request)
    return redirect('landing')

