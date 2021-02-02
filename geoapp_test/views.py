from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse("Hello, world. You're at the polls index.")




@csrf_exempt
def smartrecommender(request, **kwargs):
    begin_start_time = time.time()

    # set input parameters
    print("Im here in smartrecommender view")
    req = json.loads(request.body)
