#pages/urls.py

from django.urls import path

from .views import HomePageView, AboutPageView, TestView, ProjectsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('test/', TestView.as_view(), name='test'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('about/', AboutPageView.as_view(), name='about'),
]