from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from authentification.models import User
from flux.models import Ticket, UserFollows
from flux.forms import TicketForm

@login_required
def flux(request):
    followed_users = UserFollows.objects.filter(
        user = request.user
        ).values_list('followed_user', flat=True)
    tickets = Ticket.objects.filter(
        Q(user=request.user) | Q(user__in=followed_users)
        )
    context = {'tickets': tickets}
    return render(request, 'flux/flux.html', context=context)

@login_required
def add_ticket(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            if ticket.image and hasattr(ticket.image, 'file'):
                try:
                    ticket.resize_image()
                except Exception as e:
                    print(f"Error resizing image: {e}")
            return redirect('flux', request.user.id)
    context = {'ticket_form': ticket_form}
    return render(request, 'flux/add_ticket.html', context=context)