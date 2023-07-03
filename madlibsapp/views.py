from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.template import loader
from .forms import *

# Create your views here.
def default(request):
    return redirect("home", id=1)

def home(request,id):
    try:
        item = Story.objects.get(pk=id)
    except:
        item = Story.objects.get(pk=1)

    words = str(item)
    form = WordInputForm(request.POST)

    if(request.method == "POST"):
        if form.is_valid():
            words = item.Format(form.cleaned_data["inputWords"].split("#"))

    context={"item":words, "form":form}    

    return render(request, "madlibs/home.html", context)