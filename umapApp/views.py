from django.shortcuts import render
from django.http import HttpResponse
from umapApp.models import UrlMap
import random
# Create your views here.

def home_view(request):

    return render(request,'home.html',{})


def get_data(request, *args, **kwargs):
    rand_int = str(random.randint(1000,9999))
    long_url = None
    if request.method == 'GET':
        long_url = request.GET['key']
        p = UrlMap(longurl=long_url, shorturl=rand_int)
        p.save()
        return HttpResponse('success')

    else:
        return HttpResponse('Fail')
