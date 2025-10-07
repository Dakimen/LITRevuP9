"""
Forms module for the flux application, contains:
    class TicketForm(forms.ModelForm):
        Serves as the creation form for Ticket class objects.

    class ReviewForm(forms.ModelForm):
        Serves as the creation form for Review class objects.

    class SearchForm(forms.ModelForm):
        Serves to search for users at the subscription page of the website.
"""
from django import forms
from flux.models import Ticket, Review


class TicketForm(forms.ModelForm):
    """
    Serves to create Ticket forms to create Ticket type objects.
    Contains fields:
        title - CharField
        description - TextField
        image - ImageField
    """
    class Meta:
        """
        Meta class specifying model and fields for the TicketForm class.
        """
        model = Ticket
        fields = ['title', 'description', 'image']

    def save(self, commit=True):
        return super().save(commit=commit)


class ReviewForm(forms.ModelForm):
    """
    Serves to create Review Forms used to create Review type objects.
    Contains fields:
        headline(CharField)
        rating(ChoiceField) set to buttons saving to a SmallIntegerField.
        body(TextField)
    """
    class Meta:
        """
        Meta class defining model and fields for ReviewForm class.
        """
        model = Review
        fields = ['headline', 'rating', 'body']

    rating = forms.ChoiceField(
        choices=Review.RATING_CHOICES,
        widget=forms.RadioSelect,
    )

    def save(self, commit=True):
        return super().save(commit=commit)


class SearchForm(forms.Form):
    """
    Serves to create Search forms used to search for User instances.
    Contains fields:
        query - CharField
    """
    query = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': "Nom d'utilisateur"}
        )
    )
