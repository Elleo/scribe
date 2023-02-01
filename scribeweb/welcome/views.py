from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from shows.models import Show

def index(request):
    template = loader.get_template('index.html')
    shows = Show.objects.all()
    context = {'shows': shows}
    return HttpResponse(template.render(context, request))

def set_show(request):
    for show in Show.objects.all():
        if request.GET.get('show') != 'none' and show.id == int(request.GET.get('show')):
            show.active = True
        else:
            show.active = False
        show.save()
    return HttpResponse("ok")
