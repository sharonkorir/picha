
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
import datetime as dt
from .models import Image

# Create your views here.
def test(request):
    return HttpResponse('testing gallery')

def show_all_images(request):
    
    images = Image.get_images()
    return render(request, 'index.html', {"images":images})

#def filter_images(request,location):
    try:
        #get image by location
        images = Image.location_filter(location)
    except ValueError:
      #raise 404
      raise Http404()
      assert False

    if location == Image.location():
        return redirect()