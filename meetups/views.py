from meetups.forms import RegistrationForm
from django.shortcuts import render

from .models import Meetup
from .forms import RegistrationForm

# Create your views here.

def index(request):
  meetups = Meetup.objects.all()
  return render(request, './meetups/index.html', {
    'show_meetups': True,
    'meetups': meetups
  })

def meetup_details(request, meetup_slug):
  try:
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
    Registration_form = RegistrationForm()
    return render(request, './meetups/meetup-details.html', {
      'meetup_found': True,
      'meetup': selected_meetup,
      'form': Registration_form
    })
  except Exception as exc:
    return render(request, './meetups/meetup-details.html', {
      'meetup_found': False
    })