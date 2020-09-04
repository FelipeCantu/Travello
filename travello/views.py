from django.shortcuts import render
from .models import Destinations

# Create your views here.

def index(request):

    des_1 = Destinations()
    des_1.name = 'United States'
    des_1.desc = 'Major Atlantic Coast cities are New York'
    des_1.img = 'destination_1.jpg'
    des_1.price = 850
    des_1.offer = False

    des_2 = Destinations()
    des_2.name = 'Switzerland'
    des_2.desc = 'mountainous Central European country'
    des_2.img = 'destination_2.jpg'
    des_2.price = 650
    des_2.offer = True

    des_3 = Destinations()
    des_3.name = 'Mars'
    des_3.desc = 'fourth planet from the Sun and the second-smallest planet in the Solar System'
    des_3.img = 'destination_3.jpg'
    des_3.price = 1670
    des_3.offer = False

    dest = [des_1, des_2, des_3]

    return render(request, 'index.html', {'dest' : dest})



