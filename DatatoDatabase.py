import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("face-detection-for-atten-6b8a0-firebase-adminsdk-xakag-d48073e3d2.json")
firebase_admin.initialize_app(cred,
    {
        'databaseURL': 'https://face-detection-for-atten-6b8a0-default-rtdb.firebaseio.com/'
    }
)

ref = db.reference('Students')

data = {
    '777':{
        'Name': 'Arpit Kadam',
        'Roll_no': 777,
        'Branch': 'AIML',
        'Starting_year': 2022,
        'Marks': 97,
        'Attendance': 10,
        'Year' : 'T.E',
        'Last_attended_time' : '2022-04-01 10:00:00'
        },
    '123':{
        'Name': 'Rushikesh Injale',
        'Roll_no': 123,
        'Branch': 'CSE',
        'Starting_year': 2022,
        'Marks': 55,
        'Attendance': 3,
        'Year' : 'T.E',
        'Last_attended_time' : '2022-03-21 12:00:00'
        },
    '657':{
        'Name': 'Ana De Armas',
        'Roll_no': 657,
        'Branch': 'I.T',
        'Starting_year': 2022,
        'Marks': 78,
        'Attendance': 8,
        'Year' : 'S.E',
        'Last_attended_time' : '2022-03-23 11:00:00'
        },
    '564':{
        'Name': 'Ananya Pandey',
        'Roll_no': 564,
        'Branch': 'CHEM',
        'Starting_year': 2022,
        'Marks': 67,
        'Attendance': 8,
        'Year' : 'T.E',
        'Last_attended_time' : '2022-04-01 10:00:00'
        },
    '786':{
        'Name': 'Kiara Advani',
        'Roll_no': 786,
        'Branch': 'CSE',
        'Starting_year': 2022,
        'Marks': 67,
        'Attendance': 7,
        'Year' : 'T.E',
        'Last_attended_time' : '2022-03-28 11:00:00'
        },
    '3230':{
        'Name': 'Tripti Dimri',
        'Roll_no': 3230,
        'Branch': 'AIML',
        'Starting_year': 2022,
        'Marks': 97,
        'Attendance': 10,
        'Year' : 'T.E',
        'Last_attended_time' : '2022-04-01 10:00:00'
        },
    
}

for key,value in data.items():
    ref.child(key).set(value)