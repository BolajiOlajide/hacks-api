"""URL Definition for HACKS API."""
from django.urls import path

from .views import index, get_all_hacks

urlpatterns = [
	path('', index, name='homepage'),
	path('hacks', get_all_hacks, name='getHacks')
]
