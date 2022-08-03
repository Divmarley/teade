

from django.urls import path

from core.views import *
app_name ="web"
urlpatterns = [ 
    path('', home_view,name="index"),
    
    path('about', about_view,name="about"),
    path('service', service_view,name="service"),
    path('contact', contact_view,name="contact"),
    path('track-order', TrackView.as_view(), name="track_order"),
]