from django.urls import path
from .views import tutorial

urlpatterns = [
    path('', tutorial, name='tutorial-tutorial'),
]
