from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from events.forms import EventForm
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    return render(request, 'events/event_update.html', {'form': form})