from django.shortcuts import render

def index(request):
    context = {
        "items" : 0
    }
    return render(request,"best.html",context)


def init_map(request):
    context = {
        "items" : None
    }
    return render(request,"top.html", context)
# Create your views here.
