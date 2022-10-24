#from django.shortcuts import render
#from api.app.models import QuestionChoices
from decimal import Decimal
from re import U
from webbrowser import get
from django.http import Http404
from requests import request
from rest_framework.response import Response
from app.models import Question, QuestionChoices, User, QuestionResponse
from app.serializers import QuestionSerializer, ChoiceSerializer, UserSerializer, QuestionResponseSerializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import status, viewsets

# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailUtils(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @action(detail=True, methods=['post'])
    def get_user_id(self, request, format=None, *args, **kwargs, ):
    
        username_req = request.data["username"]
        user_info = User.objects.get(username=username_req)
        serializer = UserSerializer(user_info)
        try:
            return Response(serializer.data)
            #return User.objects.get(data)
        except User.DoesNotExist:
            raise Http404
      

class UserDetailScore(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @action(detail=True, methods=['post'])
    def add_score(self, request, format=None, *args, **kwargs, ):
        pk = self.kwargs.get('pk')
        user = self.get_user(pk)
        
        data = request.data['score']
        user.add_score(Decimal(data))
        serializer = UserSerializer(user, data={"score": user.score}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionResponseList(generics.ListCreateAPIView):
    queryset = QuestionResponse.objects.all()
    serializer_class = QuestionResponseSerializer

class QuestionResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionResponse.objects.all()
    serializer_class = QuestionResponseSerializer



# class ChoiceList(generics.ListCreateAPIView):
#     queryset = QuestionChoices.objects.all()
#     serializer_class = ChoiceSerializer

# class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = QuestionChoices.objects.all()
#     serializer_class = ChoiceSerializer