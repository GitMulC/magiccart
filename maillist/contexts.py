from .forms import MailListForm

def render_maillist_form(request):
    """ Render a mail list form for the base template """

    maillist_form = MailListForm()

    context = {
        'maillist_form': maillist_form,
    }

    return context
