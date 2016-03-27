from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Event, Attend


def index(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/event_index.html', context)

class DetailView(generic.DetailView):
    model = Event
    template_name = 'polls/event_detail.html'

def event_detail(request, id):
    event = get_object_or_404(Event, pk=id)
    attendees = Attend.objects.filter(event=event.id)

    context = {
        'event': event,
        'attendees': attendees,
    }

    return render(request, 'events/event_detail.html', context)


def event_update(request):

    context = {
        'event': event,
        'attendees': attendees,
    }

    return render(request, 'events/event_detail.html', context)