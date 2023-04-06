from django import forms
from .models import Question, QuizType, Answer

class AnswerForm(forms.Form):
    my_cheek = forms.RadioSelect()