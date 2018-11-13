import pyrebase
from geocoding_scripts import get_coord_of_address

config = {
    "apiKey": "AIzaSyCXI-9IJP7KcnhJWv-yUkAoIirUYi9P6A0",
    "authDomain": "edustats-971fc.firebaseapp.com",
    "databaseURL": "https://edustats-971fc.firebaseio.com",
    "projectId": "edustats-971fc",
    "storageBucket": "edustats-971fc.appspot.com",
    "messagingSenderId": "938636368984"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("nekorytaylor@mail.ru", "kiro2000")
db = firebase.database()

schools = db.child("educational_institutions").child("astana_kalasynyn_arbir_mektebi").get().val()

for school in schools:
        location = get_coord_of_address(school["Наименование"].replace("\\","")) 
        print(location)