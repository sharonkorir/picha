from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def test(request):
    return HttpResponse('testing gallery')

def show_all_images(request):
    
    return render(request, 'index.html')