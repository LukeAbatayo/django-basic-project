from django.urls import path

from . import views

urlpatterns = [
  path('meetups/', views.index, name='al-meetups'), # our-domain.com/meetups
  path('meetups/success', views.confirm_registration, name='confirm-registration'),
  path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail') # our-domain.com/meetups/<dynamic-path-segment>
]