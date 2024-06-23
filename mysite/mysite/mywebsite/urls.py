from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The URL pattern for the index view
]
