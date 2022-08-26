from crispy_forms.helper import FormHelper

from django import forms
from .models import Subscriber

class MailListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'

    class Meta:
        model = Subscriber
        fields = ('email',)