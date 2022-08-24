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
    
