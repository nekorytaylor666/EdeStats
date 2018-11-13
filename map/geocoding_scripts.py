import requests
import json 

def get_coord_of_address(address=None):
    if (address != None):
        params = {'address': address,
                  'key': "AIzaSyBFjzrwhH4ZL7cdUeFnRgKXyvEyIwChNmE"}
        # urllib2.urlopen('https://maps.googleapis.com/maps/api/geocode/json?' + params)
        url_list = 'https://maps.googleapis.com/maps/api/geocode/json'
        r = requests.get(url_list, params = params)
        results = r.json()['results']
        if results:
                location ={
                        "location":results[0]["geometry"]["location"],
                        "address":results[0]["formatted_address"]
                }
                return location

def get_valid_schools(school):
            location = get_coord_of_address(school["Наименование"].replace("\\","")) 
            if(location is not None and school["Средний балл "]!="-"):
                obj = {
                    "name":school["Наименование"],
                    "ent":school["Средний балл "],
                    "lat":location["location"]["lat"],
                    "lng":location["location"]["lng"],
                    "address":location["address"]
                }
                return obj
            else:
                return None