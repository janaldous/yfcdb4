from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from events.forms import EventForm
from members.models import Member
from .models import Event, Attend, ROLE


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
    members = Member.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            date = form.cleaned_data['date']
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            venue = form.cleaned_data['venue']
            new_event = Event(date=date, type=type, name=name, venue=venue)
            new_event.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(new_event.get_absolute_url())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    context = {
        'form': form,
        'members': members,
        'roles': ROLE,
    }

    return render(request, 'events/event_update.html', context)