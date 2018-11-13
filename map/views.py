from django.shortcuts import render
from .firebase import (get_schools)
from .models import School
from .geocoding_scripts import get_valid_schools
from django.db.models import Q


def index(request):

    context = {
        "items" : 0
    }
    return render(request,"best.html",context)


def init_map(request):
    # schools = get_schools()
    # for school in schools:
    #     school_dict = get_valid_schools(school)
    #     if(school_dict is not None):
    #         _name = school_dict["name"]
    #         _address = school_dict["address"]
    #         _lat = school_dict["lat"]
    #         _lng = school_dict["lng"]
    #         _ent = school_dict["ent"]
    #         print(_name)
    #         print(_address)
    #         print(_lat)
    #         print(_lng)
    #         print(_ent)
    #         obj_to_save = School(name = _name, address = _address, lat = _lat, lng = _lng, ent = _ent) 
    #         obj_to_save.save()
    schools = Schools.objects.all()

    context = {
        "schools" : schools
    }
    return render(request,"top.html", context)
# Create your views here.
