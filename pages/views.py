from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class TestView(TemplateView):
    template_name = 'test.html'

class ProjectsView(TemplateView):
    template_name = 'projects.html'

class WhateverPage(TemplateView):
    template_name = 'whatever.html'