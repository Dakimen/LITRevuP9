from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from project.forms import SignUpForm, ConnectForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def landing(request):
    if request.method == 'POST':
        connect = ConnectForm(request.POST)
        if connect.is_valid():
            email = connect.cleaned_data['email']
            password = connect.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('flux', user_id=request.user.id)
                else:
                    connect.add_error(None, 'Email ou mot de passe incorrect.')
            except User.DoesNotExist:
                connect.add_error(None, 'Email ou mot de passe incorrect.')
    else:
        connect = ConnectForm()
        return render(request,
                      'project/landing.html',
                      {'form': connect})

def sign_up(request):
    if request.method == 'POST':
        register = SignUpForm(request.POST)
        if register.is_valid():
            email = register.cleaned_data['email']
            password = register.cleaned_data['password']
            password2 = register.cleaned_data['password_2']
            if password == password2:
                if User.objects.filter(email=email).exists():
                    register.add_error(None, 'Utilisateur existe déjà.')
                else:
                    user = User.objects.create_user(username=email, email=email, password=password)
                    login(request, user)
                    return redirect('flux', user_id=request.user.id)
            else:
                register.add_error(None, 'Les mots de passe ne sont pas identiques.')
    else:
        register = SignUpForm()
        return render(request,
                      'project/sign_up.html',
                      {'form': register})

@login_required
def flux(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user:
        return HttpResponse('<p>Forbidden</p>')
    else:
        return render(request, 'project/flux.html', {'user': user})
