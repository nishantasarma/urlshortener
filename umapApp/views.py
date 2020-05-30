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
    query_set = ''
    if request.method == 'GET':
        long_url = request.GET['key']
        p = UrlMap(longurl=long_url, shorturl=rand_int)
        p.save()
        results = UrlMap.objects.all()
        #print(results[0])
        if results:
            for result in results:
                query_set = query_set + str(result) +'\r\n'

        return HttpResponse(query_set)

    else:
        return HttpResponse('Fail')
