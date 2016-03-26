from django.shortcuts import render

from .models import Event

def index(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events_list.html', context)
