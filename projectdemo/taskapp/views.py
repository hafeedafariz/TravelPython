from django.http import HttpResponse
from django.shortcuts import render
from . models import Site
from . models import School
# Create your views here.

def demo(request):
    obj1=Site.objects.all()
    obj2=School.objects.all()
    return render(request,"index.html",{'res':obj1,'sch':obj2})
