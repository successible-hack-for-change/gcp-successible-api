from django.contrib import admin
from .models import QuestionChoices, Question, User, QuestionResponse

# Register your models here.

admin.site.register(Question)
admin.site.register(QuestionChoices)
admin.site.register(QuestionResponse)
admin.site.register(User)