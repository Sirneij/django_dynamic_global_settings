from django.urls import path

from . import views

app_name: str = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('change/', views.change_settings, name='change_settings'),
]
