from django import forms
from .models import EVENT_TYPE

class EventForm(forms.Form):
    date = forms.DateField(
        input_formats=[
            '%m/%d/%Y',
            '%m/%d/%y'
        ],
        help_text="format: mm/dd/yy or mm/dd/yyyy"
    )
    name = forms.CharField(max_length=100)
    type = forms.ChoiceField(choices=EVENT_TYPE)
    venue = forms.CharField(max_length=50)