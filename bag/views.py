from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.
def view_bag(request):
    """A view to the bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add products to bag at specific quantity """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
   
    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Edit quantity of shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)
   
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        print(bag)
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
