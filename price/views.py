from django.shortcuts import render
from django.http import HttpResponse
from .models import PriceList, shortDescription

def successView(request):
    priceList = PriceList.objects.all().filter(visible=True).order_by('id')
    text = shortDescription.objects.all()[0]
    return render(request, "../templates/price.html", {'priceList': priceList, 'text': text})
