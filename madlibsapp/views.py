from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.template import loader

# Create your views here.
def default(request):
    return redirect("home", id=1)

def home(request,id):
    try:
        item = Story.objects.get(pk=id)
    except:
        item = Story.objects.get(pk=1)

    words = str(item)

    context={"item":words}

    return render(request, "madlibs/home.html", context)