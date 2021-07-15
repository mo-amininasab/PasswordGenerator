from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.generator, name='home_page'),
    path('about/', views.about, name='about_page'),
    path('show/', views.show, name='show_page'),
]