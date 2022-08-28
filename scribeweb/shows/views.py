from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import ShowForm

def index(request):
    template = loader.get_template('shows.html')
    context = {}
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    show_form = ShowForm()
    context = {'show_form': show_form}
    return HttpResponse(template.render(context, request))
