from django.conf.urls import url
from venues import views

urlpatterns = [
    url(r'venues/$', views.venue_list),
    url(r'venues/(?P<pk>[0-9]+)/$', views.venue_detail),
]