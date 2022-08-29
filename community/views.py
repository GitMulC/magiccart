from django.shortcuts import render
from .models import Community


def share_communities(request):
    """ A view to show magic the gathering sites they can use """
    communities = Community.objects.all()

    template = 'communities/communities.html'

    context = {
        'communities': communities,
    }

    return render(request, template, context)
