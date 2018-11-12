from django.shortcuts import render

def index(request):
    context = {
        "items" : 0
    }
    return render(request,"best.html",context)
# Create your views here.
