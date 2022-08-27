from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Subscriber
from .forms import MailListForm

# Create your views here.

def add_subscriber(request):
    """ Add an email to the mail list """

    form = MailListForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(request, f'{instance.email} already subscribed. Please check your email and try again.')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            instance.save()
            messages.success(request, f'{instance.email} has been added to our mail list!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
        messages.error(request, f'Error, invalid entry!')
