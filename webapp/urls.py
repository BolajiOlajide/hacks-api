"""URL Definition for HACKS Web App."""
from django.urls import path

from .views import index

urlpatterns = [
	path('add-hack', index),
]
