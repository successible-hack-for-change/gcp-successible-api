from statistics import mode
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f'{self.id}'


# Create your models here.
class Question(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=10)

    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
class QuestionSet(models.Model): 
    accessCode = models.CharField(max_length=255) 
    questions = models.ManyToManyField(Question)

class ResponseOption(models.Model): 
    text = models.CharField(max_length=255) 

class UserQuestionSet(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    questionSet = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
 
class UserResponse(models.Model): 
    user_set = models.ForeignKey(UserQuestionSet, on_delete=models.CASCADE) 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    response_option = models.ForeignKey(ResponseOption, on_delete=models.CASCADE) 
