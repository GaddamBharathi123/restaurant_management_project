from django.urls import path
from .views import *

urlpatterns = [
    path("about us/",views.about_view,name="about"),
    
]