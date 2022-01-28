from django.shortcuts import render
from .models import *
from django.db.models import Q
from home.models import *


def index(request):
    data = Company.objects.filter()
    return render(request, 'frontend/index.html', {'data': data})

def ipo(request):
    data = Company.objects.filter(type='Ipos')
    return render(request, 'frontend/ipo.html', {'data': data})
