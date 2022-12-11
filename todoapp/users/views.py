from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse(f"HELLOOOOOO {request}")
# Create your views here.
