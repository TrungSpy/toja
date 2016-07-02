from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reservation/', views.reservation, name='reservation'),
    url(r'^gather/', views.gather, name='gather'),
    url(r'^call/', views.twilio_call, name='call')
]