import  pyrebase
from firebase import  Firebase

Config = {
  'apiKey': "AIzaSyBSutK-9mJAwd_XMNOz6dS9FnwQNgtELUk",
  'authDomain': "pybase-9ca44.firebaseapp.com",
  'databaseURL': "https://pybase-9ca44-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "pybase-9ca44",
  'storageBucket': "pybase-9ca44.appspot.com",
  'messagingSenderId': "122039507185",
  'appId': "1:122039507185:web:1bc2e56ebcf039b3cc3150",
  'measurementId': "G-JXVYRD8CVM"
};

firebase = Firebase(Config)
db = firebase.database()

data = {"name":"sk",
        "date": "today"}

db.set(data)