from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse(f"HELLOOOOOO {request}")


def register(request, username, password):
    print(username, password)
    # Create your views here.
