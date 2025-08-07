from django.shortcuts import render
from .models import Menultem

def homepage(request):
    menu_items = Menultem.objects.all()
    return render(request,'home.html',{'menu_items':menu_items})
    
