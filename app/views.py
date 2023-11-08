from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def swag(request):
    return HttpResponse('<h1><marquee>Hi rani </h1></marquee>')

def bindu(request):
    return HttpResponse('<h1><marquee>How r u</h1></marquee>')
