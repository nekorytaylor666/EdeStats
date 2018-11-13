import pyrebase

def init_db():  
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
    user = auth.sign_in_with_email_and_password("olzhas2201@gmail.com", "sultan2008")
    db = firebase.database()
    print(db)
    return db

def get_schools():
    db = init_db()
    schools = db.child("educational_institutions").child("astana_kalasynyn_arbir_mektebi").get().val()
    return schools

