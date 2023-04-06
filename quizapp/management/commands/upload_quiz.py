import csv

from django.core.management.base import BaseCommand, CommandError
from quizapp.models import Question, QuizType, Answer

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        file_path = options.get('file')
        with open(file_path, 'r') as file:
            data = csv.reader(file, delimiter=',')
            for row in data:
                quiz_type, _ = QuizType.objects.get_or_create(name=row[0])
                question = Question.objects.create(quiz_type=quiz_type, name=row[1])
                Answer.objects.create(question=question, name=row[2], is_right=True)
                Answer.objects.create(question=question, name=row[3], is_right=False)
                Answer.objects.create(question=question, name=row[4], is_right=False)
                Answer.objects.create(question=question, name=row[5], is_right=False)
        print('succesfully')
