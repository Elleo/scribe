from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('shows.html')
    context = {}
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    context = {}
    return HttpResponse(template.render(context, request))
