from django.shortcuts import render, get_object_or_404
from .models import Card

# Create your views here.
def all_cards(request):
    """A view to show all card products & incl searching and sorting"""

    cards = Card.objects.all()

    context = {
        'products': cards,
    }

    return render(request, 'cards/cards.html', context)

def card_detail(request, card_id):
    """A view to show each individual card details"""

    card = get_object_or_404(Card, pk=card_id)

    context = {
        'product': card,
    }

    return render(request, 'cards/card_detail.html', context)   
