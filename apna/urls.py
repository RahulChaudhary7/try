from django.urls import path 
from . import views

urlpatterns = [
    path("",views.stud,name="stud")
]
