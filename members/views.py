from django.shortcuts import render
from .models import Member


def index(request):
    members = Member.objects.all()

    context = {
        'members': members,
    }

    return render(request, 'members/member_index.html', context)

def member_detail(request, id):
    member = Member.objects.get(pk=id)

    context = {
        'member': member,
    }

    return render(request, 'members/member_detail.html', context)