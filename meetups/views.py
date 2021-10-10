from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
        {
            'title': 'A First Meetup', 
            'location': 'New York', 
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Secont Meetup', 
            'location': 'Paris', 
            'slug': 'a-second-meetup'
        }
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
