# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('download-csv/', views.download_csv, name='download-csv'),
]
