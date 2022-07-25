from django.contrib.auth.models import AbstractUser
from django.db import models
from db.models import BaseModel


class User(AbstractUser, BaseModel):
    full_name = models.CharField(max_length=256, null=True)
