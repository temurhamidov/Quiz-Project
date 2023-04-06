from django.contrib import admin
from .models import QuizType, Question, Answer, Result
# Register your models here.

@admin.register(QuizType)
class QuizTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_right', 'question']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_right']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'quiz_type']
    inlines = [AnswerInlineModel]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_question', 'correct_question', 'created', 'quiz']



