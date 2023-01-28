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

def add_or_edit(request):
    values = convert_post_items(request.POST.items())
    show_id = request.GET.get('id')
    title = "Add Show"
    edit = False
    if request.POST.get('delete') is not None:
        if show_id is not None:
            Show.objects.get(id=show_id).delete()
        return redirect("/shows")
    elif request.POST.get('submit') is not None:
        if show_id is not None:
            show = Show.objects.get(id=show_id)
            edit = True
            title = show.name
            show_form = ShowForm(data=request.POST, instance=show)
        else:
            show_form = ShowForm(data=request.POST)
        if show_form.is_valid():
            show = show_form.save()
            if 'script_file' in request.FILES:
                show.script = request.FILES['script_file'].read().decode()
                show.save()
            return redirect("/shows")
        else:
            context = {'show_form': show_form, 'edit': edit, 'title': title}
            return HttpResponse(template.render(context, request))
    else:
        if show_id is not None:
            show = Show.objects.get(id=show_id)
            show_form = ShowForm(initial=model_to_dict(show))
            title = show.name
            edit = True
        else:
            show_form = ShowForm
        template = loader.get_template('add.html')
        context = {'show_form': show_form, 'edit': edit, 'title': title}
        return HttpResponse(template.render(context, request))
