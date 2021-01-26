from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> this is second github of prabin</h1>")
def home(request):
    return HttpResponse("<h2>this is home page</h2>")
def gallery(request):
    return HttpResponse("<h3>this is gallery</h3>")
