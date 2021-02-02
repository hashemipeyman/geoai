from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
import time
import psycopg2
import psycopg2.extras
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.


def index(request):
    print(request)
    return HttpResponse("Hello, world. You're at the polls index.")




@csrf_exempt
def smartrecommender(request, **kwargs):
    begin_start_time = time.time()

    # set input parameters
    input_search_text = request.POST['search']


    context = {}
    context['input_search_text'] = input_search_text
    return JsonResponse(context, encoder=JSONEncoder)
