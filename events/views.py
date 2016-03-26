from django.shortcuts import render

from .models import Event

def index(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/event_index.html', context)

def event_detail(request, id):
    event = Event.objects.get(pk=id)
    attendees = event.attendees.all()

    context = {
        'event': event,
        'attendees': attendees,
    }

    return render(request, 'events/event_detail.html', context)