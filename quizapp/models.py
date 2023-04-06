from django.db import models
from user.models import User
from django.utils.text import slugify

# Create your models here.

class QuizType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'QuizType'
        verbose_name_plural = 'QuizTypes'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(QuizType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz_type = models.ForeignKey(QuizType, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Result(models.Model):
    total_question = models.IntegerField()
    correct_question = models.IntegerField()
    quiz = models.ForeignKey(QuizType, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @property
    def total(self):
        return round(100 * self.correct_question / self.total_question, 2)


