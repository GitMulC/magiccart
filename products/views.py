from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Card, Type

# Create your views here.
def all_cards(request):
    """A view to show all card products & incl searching and sorting"""

    cards = Card.objects.all()
    query = None
    types = None

    if request.GET:
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            cards = cards.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
               messages.error(request, "You didn't enter any search criteria!")
               return(redirect(reverse('products')))

            queries = Q(name__icontains=query) | Q(rarity__icontains=query)
            cards = cards.filter(queries)

    context = {
        'products': cards,
        'search_term': query,
        'current_types': types,
    }

    return render(request, 'cards/cards.html', context)


def card_detail(request, card_id):
    """A view to show each individual card details"""

    card = get_object_or_404(Card, pk=card_id)

    context = {
        'product': card,
    }

    return render(request, 'cards/card_detail.html', context)
