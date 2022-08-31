from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import ShowForm
from .models import Show

def convert_post_items(items):
    values = {}
    for key, val in items:
        if val == '':
            values[key] = None
        elif val == 'true' or val == 'on':
            values[key] = True
        elif val == 'false':
            values[key] = False
        else:
            values[key] = val
    return values

def index(request):
    template = loader.get_template('shows.html')
    shows = Show.objects.all()
    context = {'shows': shows}
    return HttpResponse(template.render(context, request))

def add(request):
    values = convert_post_items(request.POST.items())
    if request.POST.get('submit') is not None:
        image = request.FILES.get('image')
        if image is not None:
            show = Show.objects.create(
                    name=values.get('name'),
                    image=image,
                    language=values.get('language'),
                    script=values.get('script'),
                    prioritise_accuracy=values.get('prioritise_accuracy', False)
            )
        else:
            # Work around ImageField not accepting None correctly
            show = Show.objects.create(
                    name=values.get('name'),
                    language=values.get('language'),
                    script=values.get('script'),
                    prioritise_accuracy=values.get('prioritise_accuracy', False)
            )
        return redirect("/shows")
    else:
        edit = False
        title = "Add Show"
        if request.GET.get('id') is not None:
            show = Show.objects.get(id=request.GET.get('id'))
            show_form = ShowForm(initial=model_to_dict(show))
            title = show.name
            edit = True
        else:
            show_form = ShowForm
        template = loader.get_template('add.html')
        context = {'show_form': show_form, 'edit': edit, 'title': title}
        return HttpResponse(template.render(context, request))
