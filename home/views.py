from django.shortcuts import render
from .models import Menultem
from rest_framework.decorators import api_view
from rest_framework.response import Response

def homepage(request):
    menu_items = Menultem.objects.all()
    return render(request,'home.html',{'menu_items':menu_items})
@api_view(['GET'])
def get_menu(request):
    menu_data = [
        {'name':'Paneer Butter Masala','description':'Cottage cheese cooked in creamy tomato gravy','price':180.00},
        {'name':'Chicken Biryani','descrition':'Basmati rice with spiced chicken','price':220.00},
        {'name':'Veg Fried Rice','descrition':'Fried rice with fresh vegetables and soy sauce','price':130.00},]
    return Response(menu_data)        
    
