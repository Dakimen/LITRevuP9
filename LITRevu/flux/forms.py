from django import forms
from flux.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

    def save(self, commit=True):
        print("[TicketForm] save called with commit =", commit)
        return super().save(commit=commit)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']

    
    rating = forms.ChoiceField(
        choices=Review.RATING_CHOICES,
        widget=forms.RadioSelect,
    )

    def save(self, commit=True):
        print("Review_form save called with commit =", commit)
        return super().save(commit=commit)


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': "Nom d'utilisateur"}
        )
    )


class SubscriptionForm(forms.Form):
    subscribed = forms.BooleanField()
