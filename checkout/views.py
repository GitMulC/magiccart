from django.shortcuts import render, redirect, reverse

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag at the moment")
        return redirect(request('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LXp45G7PugiIHvNxfZUr49w3sNZ3c1h92iDQVh5E08omMd8QRBb6fYJ2mvnZskW5vF8ewHQolM4Zrylz39pODGF00wobI9XFl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
