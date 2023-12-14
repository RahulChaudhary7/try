from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.

def stud(request):
    abc = language.objects.all()
    temp = loader.get_template("first.html")
    print(abc)
    cont = {
        "ab" : abc
    }
    return HttpResponse(temp.render(cont , request))

def second(request):
    if request.method == 'POST':
        name = request.POST.get("lname")
        img = request.FILES.get("image")

        s = language()
        s.name = name
        s.photo = img
        s.save()
        return redirect("/")
    return render(request , "langadd.html")