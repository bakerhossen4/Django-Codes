from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home (request ) :
    return HttpResponse('App1/')
def Contact( request ):
    return HttpResponse('App1/Contact Page')