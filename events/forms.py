from django import forms

from members.models import Member
from .models import EVENT_TYPE, ROLE

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

class AttendForm(forms.Form):
    #names
    member = forms.ForeignKey(Member)
    role = forms.CharField(choices=ROLE)