from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class StrainHomeView(TemplateView):
    template_name = 'strain_home.html'
