from django.shortcuts import render
from django.http import JsonResponse


def index (request):
    data = [{
        "name" : "Abel Flomo",

        "Track" : "Backend(python)",

        "message" : "Hi, Instructor. Thanks so much. You are doing a great job",
    }]
    return JsonResponse ({'data':data})
