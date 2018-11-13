from models import School
from geocoding_scripts import get_valid_schools
from firebase import get_schools

schools = get_schools()
for school in schools:
    school_dict = get_valid_schools(school)
    if(school_dict is not None):
        name = school_dict["name"]
        address = school_dict["address"]
        lat = school_dict["lat"]
        lng = school_dict["lng"]
        ent = school_dict["ent"]
        print(name)
        print(address)
        print(lat)
        print(lng)
        print(ent)
        #School.save(name=name, address= address, lat = lat, lng = lng, ent = ent)   