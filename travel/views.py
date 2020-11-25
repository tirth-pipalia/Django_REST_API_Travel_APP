from django.shortcuts import render
from .models import travelling
from django.http import HttpResponse

# Create your views here.
def index(request):
    des = travelling.objects.all()
    return render(request, 'all.html',{'places':des})

def typography(request):
    return render(request, 'typography.html')

def about(request):
    return render(request, 'about.html')