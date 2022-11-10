# Successible-Api

This is the api for the Successible Project

### Pre-Requisite:
Python 3.10.4

In this project we used django, django rest framework. Please follow the installation guide below to run it locally

## Installation

### For windows to activate env
1. Go into the Successible-Api repo then run commands
```
    py -m venv env
    Set-ExecutionPolicy Unrestricted -Scope Process
    env\Scripts\activate
```
```
    py -m pip install -r requirements.txt
```

### For Mac
1. Go into the Successible-Api repo then run commands:
```
    python3 -m venv env  
    source env/bin/activate
```
```
    python3 -m pip install -r requirements.txt 
```

## Running the api

To run the app (for windows replace python3 with py):

```
    python3 manage.py makemigrations app
    python3 manage.py migrate app
    python3 manage.py migrate   

    python3 manage.py runserver 
```

## Endpoints - details of the APIs

```
host: successible-api-nqnaexycua-nw.a.run.app
```

### Questions API

1. Return all questions:

    In the headers, you will need to include a valid Access-Code value
```
GET https://{host}/questions
```
2. To post a question:
```
POST https://{host}/
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
```

### Users API

1. List of all Users
```
GET https://{host}/users
```

2. Create user
```
POST http:s//{host}/users
{
    "username" : "a",
    "email" : "a@email.com"
}
```

3. View User Details
```
GET https://{host}/user/<int:pk>
```

### Question Responses API

1. To submit a response from the user
```
POST https://{host}/user/<int:pk>/postresponse
{
    "user" : 1,
    "questionId" : 5,
    "candidateAnswer" : "A"
}
```

2. When the test finishes - this submits the form and calculates the score, where 1 is <int:pk>
```
GET https://{host}/user/1/postresponse
```
### Notes for developing

1. To retrieve userID by username
```
POST https://{host}/getuser
{
    "username" : "a"
}
```
