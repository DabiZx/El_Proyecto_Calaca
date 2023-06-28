from django.urls import path

from core import views

urlpatterns = [
    path('index/', views.IndexView, name = 'index'),
]