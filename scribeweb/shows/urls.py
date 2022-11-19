from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('add/', views.add_or_edit, name='add'),
        path('edit/', views.add_or_edit, name='edit'),
]
