from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from shows.models import Show

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    shows = Show.objects.all()
    context = {'shows': shows}
    return HttpResponse(template.render(context, request))
