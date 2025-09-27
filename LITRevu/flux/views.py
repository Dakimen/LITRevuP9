from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from authentification.models import User
from flux.models import Ticket, UserFollows
from flux.forms import TicketForm, ReviewForm

@login_required
def flux(request):
    followed_users = UserFollows.objects.filter(
        user = request.user
        ).values_list('followed_user', flat=True)
    tickets = Ticket.objects.filter(
        Q(author=request.user) | Q(author__in=followed_users)
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
            ticket.author = request.user
            ticket.save()
            return redirect('flux')
    context = {'ticket_form': ticket_form}
    return render(request, 'flux/add_ticket.html', context=context)

@login_required
def add_review(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.author = request.user
            review.save()
            return redirect('flux')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form
    }
    return render(request, 'flux/add_review.html', context=context)
