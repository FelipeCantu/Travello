from django.shortcuts import render
from .models import Destinations

# Create your views here.

def index(request):

    dest = Destinations.objects.all()

    return render(request, 'index.html', {'dest' : dest})



