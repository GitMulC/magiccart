from django.shortcuts import render
from .models import Event


def show_events(request):
    """ A view to show magic the gathering events going on """
    events = Event.objects.all()

    template = 'events/events.html'

    context = {
        'events': events,
    }

    return render(request, template, context)
