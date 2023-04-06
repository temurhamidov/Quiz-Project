import random
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from user.models import User
from .mixins import StudentRequiredMixin, TeacherRequiredMixin, TeacherAndStudentRequiredMixin
from .models import QuizType, Question, Answer, Result

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'quizapp/home.html')



class QuizTypeView(TeacherAndStudentRequiredMixin, ListView):
    queryset = QuizType.objects.all()
    template_name = 'quizapp/quiz_type_list.html'


def error_403(request, exception):
    return render(request, '403.html')

def error_404(request, exception):
    return render(request, '404.html')


# class QuestionList(View):
#     def get(self, request, *args, **kwargs):
#         quiz_type_slug = self.kwargs.get('slug')
#         questions = Question.objects.filter(quiz_type__slug=quiz_type_slug)
#         questions = random.sample(list(questions), 5)
#         answer = Answer.objects.filter(question__in=questions)
#         answer = list(answer)
#         random.shuffle(answer)
#         context = {
#             'questions': questions,
#             'answer': answer,
#         }
#         return render(request, 'quizapp/question_list.html', context)
#
#     def post(self, request):
#         result = Result()
#         answer_name = request.POST.get()
#         result.user = request.user
#         # result.save()
#         return redirect('quizapp:home_view')


def QuestionListView(request, *args, **kwargs):
    quiz_type_slug = kwargs.get('slug')
    questions = Question.objects.filter(quiz_type__slug=quiz_type_slug)
    questions = random.sample(list(questions), 5)
    answer = Answer.objects.filter(question__in=questions)
    answer = list(answer)
    random.shuffle(answer)
    if request.method == 'POST':
        q_len = len(questions)
        correct = 0
        wrong = 0
        for q in questions:
            if request.POST.get(q.name) == "True":
                correct += 1
            else:
                wrong += 1
            quiz_type = q.quiz_type
        result = Result()
        result.user = request.user
        result.correct_question = correct
        result.total_question = q_len
        result.quiz = quiz_type
        result.save()
        context = {
            'correct' : correct,
            'total_question' : len(questions),
            'wrong' : wrong,
            'user' : request.user,
            'quiz_type' : quiz_type,
            'total' : round(correct * 100 / q_len, 2)
        }
        return render(request, 'quizapp/result.html', context)
    context = {
        'questions': questions,
        'answer': answer,
    }
    return render(request, 'quizapp/question_list.html', context)


class ResultList(View):
    def get(self, request, *args, **kwargs):
        results = Result.objects.all()
        context = {
            'results' : results,
        }
        return render(request, 'quizapp/result_list.html', context)



