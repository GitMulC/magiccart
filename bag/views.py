from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """A view to the bag page"""

    return render(request, 'bag/bag.html')
