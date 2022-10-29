# Successible-Api

For windows to activate env
1. Go into the Successible-Api repo then run commands
python3 -m venv env
Set-ExecutionPolicy Unrestricted -Scope Process
env\Scripts\activate
2. cd into the api folder
py -m pip install -r requirements.txt 

For mac
1. Go into the Successible-Api repo then run commands
python3 -m venv env  
source env/bin/activate
2. cd into the api folder then run the following
python3 -m pip install -r requirements.txt 

To run the app cd into the api folder and run the following commands

python3 manage.py makemigrations app
python3 manage.py migrate app
python3 manage.py migrate   

python3 manage.py runserver 


Endpoints - details of the APIs

Questions API

Return all questions
GET http://127.0.0.1:8000/ 

POST http://127.0.0.1:8000/
{
    "question": "Example question",
    "answer": "A",
    "resA": "3",
    "resB": "4",
    "resC": "5",
    "resD": "6",
    "highlight": "7",
    "image": "8",
    "timeLimit": 120,
    "definitions": "defn"
}

Users API

List of all Users
GET http://127.0.0.1:8000/users

Create user
POST http://127.0.0.1:8000/users
{
    "username" : "a",
    "email" : "a@email.com"
}

View User Details
GET http://127.0.0.1:8000/user/<int:pk>

Question Responses API

To submit a response from the user
POST http://127.0.0.1:8000/user/<int:pk>/postresponse
{
    "user" : 1,
    "questionId" : 5,
    "candidateAnswer" : "A"
}

When the test finishes - this submits the form and calculates the score, where 1 is <int:pk>
GET http://127.0.0.1:8000/user/1/postresponse

Notes

In case:
to retrieve userID by username

POST http://127.0.0.1:8000/getuser
{
    "username" : "a"
}