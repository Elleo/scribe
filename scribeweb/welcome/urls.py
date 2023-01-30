from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('set_show', views.set_show, name='set_show'),
]
