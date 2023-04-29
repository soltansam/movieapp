from django.shortcuts import render
from django.http import HttpResponse



def about(request):
   return HttpResponse('<h1> Welcome to about page </h1>')

def home(request):
   return render(request, 'home.html', {'name': 'Sam'} )