from django.urls import path
from .views import main, about

urlpatterns = [
    path('', main, name='home-home'),
    path('about/', about, name='home-about')
]
