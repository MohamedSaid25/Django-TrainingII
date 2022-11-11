from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=256)

    class Meta:
        db_table = 'Users'
