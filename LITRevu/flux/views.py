from itertools import chain
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from authentification.models import User
from flux.models import Ticket, UserFollows, Review
from flux.forms import TicketForm, ReviewForm, SearchForm

@login_required
def flux(request):
    followed_users = UserFollows.objects.filter(
        user = request.user
        ).values_list('followed_user', flat=True)
    tickets = Ticket.objects.filter(
        Q(author=request.user) | Q(author__in=followed_users)
        )
    reviews = Review.objects.filter(
        Q(author=request.user) | Q(author__in=followed_users)
    )
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    context = {'tickets_and_reviews': tickets_and_reviews}
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

@login_required
def add_review_to_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    review_form = ReviewForm()
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.author = request.user
            review.save()
            return redirect("flux")
    context = {"ticket": ticket, "review_form": review_form}
    return render(request, 'flux/add_review_to_ticket.html', context=context)

@login_required
def subscriptions(request):
    follow_pairs_followed = UserFollows.objects.filter(followed_user=request.user)
    follow_pairs_following = UserFollows.objects.filter(user=request.user)
    subscribers = []
    subscribed_to = []
    search_form = SearchForm()
    for follow_pair in follow_pairs_followed:
        subscribers.append(follow_pair.user)
    for follow_pair in follow_pairs_following:
        subscribed_to.append(follow_pair.followed_user)
    if request.method == "GET":
        if search_form.is_valid():
            search_form = SearchForm(request.GET)
            query = search_form.cleaned_data["query"].strip()
            results = User.objects.filter(username__icontains=query)
            context = {
                'search_form': search_form,
                'results': results,
                'subscribers': subscribers,
                'subscribed_to': subscribed_to}
            return render(request, 'flux/subscriptions.html', context=context)
        else:
            results = []
            context = {
                'search_form': search_form,
                'results': results,
                'subscribers': subscribers,
                'subscribed_to': subscribed_to}
    return render(request, 'flux/subscriptions.html', context=context)

@login_required
def my_posts(request):
    own_reviews = Review.objects.filter(author=request.user)
    own_tickets = Ticket.objects.filter(author=request.user)
    tickets_and_reviews = sorted(
        chain(own_tickets, own_reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    context = {'tickets_and_reviews': tickets_and_reviews}
    return render(request, 'flux/own_posts.html', context=context)
