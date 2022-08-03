import re
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q

from core.models import Track

# Create your views here. 
def home_view(request):
    template_name='home.html'
    # search_post = request.GET.get('search')
 
    # if search_post:
    #     posts = Track.objects.filter(Q(tracking_id__icontains=search_post))
    # else:
    #     # If not searched, return default posts
    #     # posts = Track.objects.all() 
    return render(request,template_name,{})

def send(request):
    if request.method == 'POST':
        
        dict = {
        }
        return render(request, 'track_order.html', dict)
        
    

def about_view(request):
    template_name='about.html'
    context={}
    return render(request,template_name,context)

def service_view(request):
    template_name='service.html'
    context={}
    return render(request,template_name,context)

def contact_view(request):
    template_name='contact.html'
    context={}
    return render(request,template_name,context)

# def track_order_view(request):
#     template_name='track_order.html'
#     context={}
#     return render(request,template_name,context)


class TrackView(View):   
    model = Track
    template_name = 'track_order.html'
    # context_object_name = 'all_search_results'

    def get(self,request):
        return render(request,self.template_name,{})


    def post(self,request):
        return render(request,self.template_name,{})