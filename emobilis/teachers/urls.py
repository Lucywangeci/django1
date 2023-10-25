from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('contact', views.Contact),
    path('help', views.Help)
]