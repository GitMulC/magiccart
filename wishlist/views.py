from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Card


@login_required
def display_wishlist(request):
    """ A view for showing a user all their wishlist items """
    wishlist_item = Card.objects.filter(user_favorite=request.user)

    context = {
        'wishlist_item': wishlist_item,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, card_id):
    """ A view to add cards to your wishlist """
    card = get_object_or_404(Card, id=card_id)

    if card.user_favorite.filter(id=request.user.id).exists():
        card.user_favorite.remove(request.user)
        messages.success(request,
                         f'{card.name} has been \
                         removed from your wishlist.')
    else:
        card.user_favorite.add(request.user)
        messages.success(request,
                         f'{card.name} has been \
                         added from your wishlist.')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
