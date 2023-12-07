from django.shortcuts import render
from django.http import JsonResponse


def index (request):
    data = [{
        "name": "Abel Flomo \n",

        "Track" : "Backend(python) \n",

        "message": "Hi, Instructor. Thanks so much. You are doing a great job \n ",
    }]
    return JsonResponse ({'data':data})
