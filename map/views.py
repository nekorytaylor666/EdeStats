from django.shortcuts import render

def index(request):
    context = {
        "items" : 0
    }
    return render(request,"base.html",context)
# Create your views here.
