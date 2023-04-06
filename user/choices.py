from django.db import models

class UserType(models.IntegerChoices):
    ADMIN = 0, 'Admin'
    STUDENT = 1, 'Student'
    TEACHER = 2, 'Teacher'


class Gender(models.IntegerChoices):
    NOT_SPECIFED = 0, 'Not specifed'
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'

