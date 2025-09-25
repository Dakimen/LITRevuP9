from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from authentification.models import User

@login_required
def flux(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user != user:
        return HttpResponse('<p>Forbidden</p>')
    else:
        return render(request, 'flux/flux.html', {'user': user})
