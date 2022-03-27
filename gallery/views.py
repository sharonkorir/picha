
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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("imahe")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})