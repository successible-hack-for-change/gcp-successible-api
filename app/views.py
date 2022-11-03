#from django.shortcuts import render
#from api.app.models import QuestionChoices
from decimal import Decimal
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
    
class CustomQuestionList(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    @action(detail=True, methods=['get'])
    def get_question_list(self, request, format=None, *args, **kwargs):
        
        accessCode = request.headers.get("Access-Code")
        if accessCode == "test" or accessCode == "demo" or accessCode == "nKNjpC4P" or accessCode == "9k8ZE6g8":
            query = Question.objects.all()
            serializer = QuestionSerializer(query, many=True )
            return Response(serializer.data)
        return Response("Please check users access code",status=status.HTTP_404_NOT_FOUND )
        
        

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
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    @action(detail=True, methods=['post'])
    def get_user_id(self, request, format=None, *args, **kwargs):
    
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
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    @action(detail=True, methods=['post'])
    def add_score(self, request, format=None, *args, **kwargs):
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

class QuestionResponseAPI(viewsets.ModelViewSet):
    queryset = QuestionResponse.objects.all()
    serializer_class = QuestionResponseSerializer

    def check_result(self, questionId, candidateAnswer):
        print("questionId is " + str(questionId))
        query = Question.objects.filter(id=questionId)
        #print(query[0].answer)
        
        if query.count() == 1:
            if query[0].answer == candidateAnswer:
                print("True")
                return True
        print("False")
        return False


    @action(detail=True, methods=['post'])
    def post_result(self, request, format=None, **kwargs):
        reqUser = request.data['user']
        reqQuestion = request.data['questionId']
        reqCandidateAnswer = request.data['candidateAnswer']
        
        pk = self.kwargs.get('pk')
        
        if reqUser != pk:
            return Response("User id and pk mismatch, please check and try again",status=status.HTTP_400_BAD_REQUEST)

        if QuestionResponse.objects.filter(questionId=reqQuestion).filter(user=reqUser).count() == 0:
            print("QuestionResponse does not exist in db, question was not answered by user before")
            if self.check_result(reqQuestion, reqCandidateAnswer):
                request.data['correct'] = True
            serializer = QuestionResponseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("QuestionResponseSerializer is valid and saved")
                return Response(serializer.data)
            else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.check_result(reqQuestion, reqCandidateAnswer)
        return Response("Error 412: a response for this question has already been received. Please check and try again", status=status.HTTP_412_PRECONDITION_FAILED)

    @action(detail=True, methods=['get'])
    def get_score_sheet(self, format=None, **kwargs):
        # reqUser = request.data['user']
        pk = self.kwargs.get('pk')
        query = QuestionResponse.objects.filter(user=pk)

        correctAnswers = query.filter(correct=True).count()
        print(pk)
        user = User.objects.get(id=pk)
        user.score = user.set_score(correctAnswers)
        userSerial = UserSerializer(user, data={"score": user.score}, partial=True)
        if userSerial.is_valid():
            userSerial.save()

        serializer = QuestionResponseSerializer(query, many=True)

        sortedQuery = query.order_by('questionId_id')
        print(sortedQuery)

        if sortedQuery.count() != 0:
            n = f'Username: {user.get_username()}'
            s = f'Score: {100.0 * user.score/sortedQuery.count()}%'
            s3 = ""

            for i in sortedQuery:
                s3 = '\n'.join([s3,f"Question {i.questionId.id} : {i.candidateAnswer}"])

            s4 = '\n'.join([n, s, s3])
            print(s4)
            return Response(serializer.data)
        elif sortedQuery.count() == 0:
            return Response("Sorry an error has occurred, please check responses have been submitted or try again later", status=status.HTTP_412_PRECONDITION_FAILED)
        return Response("Sorry an error has occurred, please try again later", status=HTTP_500_INTERNAL_SERVER_ERROR)
    