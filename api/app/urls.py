from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

user_score = views.UserDetailScore.as_view({
    'post': 'add_score',
})

user_utils = views.UserDetailUtils.as_view({
    'post': 'get_user_id',
})

urlpatterns = [
    path('', views.QuestionList.as_view()),
    path('question/<int:pk>/', views.QuestionDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('user/<int:pk>/score', user_score),
    path('user/<int:pk>/responses', views.QuestionResponseList.as_view()),
    path('user/<int:pk>/response/<int:pk_2>/', views.QuestionResponseDetail.as_view()),
    path('getuser', user_utils),

    # path('choices/', views.ChoiceList.as_view()),
    # path('choices/<int:pk>/', views.ChoiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
