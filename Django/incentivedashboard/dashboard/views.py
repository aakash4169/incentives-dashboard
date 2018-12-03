from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index (request):
    template = loader.get_template('dashboard/index.html')
    return HttpResponse(template.render(request, 'dashboard/index.html'))

# Create your views here.
