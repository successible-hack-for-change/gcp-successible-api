from asyncore import read
from operator import mod
from optparse import Option
from secrets import choice
from rest_framework import serializers
from app.models import Question, User, QuestionChoices, QuestionResponse


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'score', 'accessCode']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = QuestionChoices

class QuestionSerializer(serializers.ModelSerializer):
    #choices = ChoiceSerializer()
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'resA', 'resB', 'resC', 'resD', 'highlight', 'image', 'timeLimit', 'definitions']

class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'user', 'questionId', 'candidateAnswer', 'correct']
        model = QuestionResponse