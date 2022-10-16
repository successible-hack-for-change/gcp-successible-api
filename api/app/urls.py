from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('app/', views.QuestionList.as_view()),
    path('app/<int:pk>/', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
