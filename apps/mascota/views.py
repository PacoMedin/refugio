from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""def index_mascota(request):
    return HttpResponse("Index mascota")"""

def index_mascota(request):
    return render(request, 'mascota/index.html')

