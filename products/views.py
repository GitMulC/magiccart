from django.shortcuts import render
from .models import Card

# Create your views here.
def all_cards(request):
    """A view to show all card products & incl searching and sorting"""

    cards = Card.objects.all()

    context = {
        'products': cards,
    }

    return render(request, 'cards/cards.html', context)
