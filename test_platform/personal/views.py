from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# MVT -- V

def say_hello(request):
    name = request.GET.get("name", "")
    talk = ""
    for n in range(3):
        talk = talk + "Hello," + name + "\n"
    return HttpResponse(talk)
