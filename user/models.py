from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import UserType, Gender

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    user_type = models.IntegerField(default=UserType.ADMIN, choices=UserType.choices)
    gender = models.IntegerField(default=Gender.NOT_SPECIFED, choices=Gender.choices)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None
