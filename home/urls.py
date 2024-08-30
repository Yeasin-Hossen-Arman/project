from django.contrib import admin
from django.urls import path

from home import views
from home.views import *

urlpatterns = [
    path("",views.index , name="home"),
    path("result", result, name="result"),  
]