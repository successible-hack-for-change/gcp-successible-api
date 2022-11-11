# Successible-Api

This is the api for the Successible Project. Further details can be found at our front end repository https://github.com/successible-hack-for-change/successible

This respository is for the version running on GCP and we have a different respository for running locally https://github.com/successible-hack-for-change/Successible-Api/tree/demo

### Pre-Requisite:
Python 3.10.4

In this project we used django and django rest framework. The following describes the end points 


```
host: successible-api-nqnaexycua-nw.a.run.app
```

## Endpoints - details of the APIs

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
