from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .wifi import Wifi

# Create your views here.
def index(request):
    template = loader.get_template('settings.html')
    wifi = Wifi()
    context = {'networks': wifi.networks,
            'current_network': wifi.current_network}
    return HttpResponse(template.render(context, request))
