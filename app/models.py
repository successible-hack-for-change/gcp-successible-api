from enum import unique
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from pkg_resources import require

class User(AbstractUser):
    score = models.IntegerField(blank=True, null=True, default= 0)
    accessCode = models.CharField(max_length=255, blank=True, default='')
    def __str__(self):
        return f'{self.id}'
    
    def get_score(self):
        return self.score
    
    def add_score(self, amount):
        self.score += amount
        return self.score

    def set_score(self, amount):
        self.score = amount
        return self.score
    
    def get_access_code(self):
        return self.access_code

    def set_access_code(self, code):
        self.access_code = code
        return self.access_code

    def get_username(self) -> str:
        return super().get_username()


# Create your models here.
class Question(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=10)
    resA = models.CharField(max_length=255)
    resB = models.CharField(max_length=255)
    resC = models.CharField(max_length=255)
    resD = models.CharField(max_length=255)
    highlight = models.TextField()
    image = models.CharField(max_length=255)
    timeLimit = models.IntegerField()
    definitions = models.TextField()
    
    def __str__(self):
        return "question: " +  self.question + ", answer" + self.answer
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class QuestionChoices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text


class QuestionSet(models.Model): 
    accessCode = models.CharField(max_length=255) 
    questions = models.ManyToManyField(Question)


class QuestionResponse(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    candidateAnswer = models.CharField(max_length=255)
    correct = models.BooleanField(blank=True, default=False)

# class AnswerResponse(models.Model):
#     user  = models.ForeignKey(User, on_delete=models.CASCADE)
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#     candidate_answer = models.CharField(max_length=255)
#     correct = models.BooleanField()
