from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'homepage.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CantactPageView(TemplateView):
    template_name = 'cantact.html'

class WorkPageView(TemplateView):
    template_name = 'staj.html'