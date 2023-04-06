from django.urls import path
from .views import HomeView, QuestionListView, ResultList, QuizTypeView

app_name = 'quizapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('quiz-type', QuizTypeView.as_view(), name='quiz_type_list'),
    path('question-list/<slug:slug>', QuestionListView, name='question_list'),
    path('result-list/', ResultList.as_view(), name='result_list'),

]