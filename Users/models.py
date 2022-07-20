from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=13)
    options = (
        ("employer", "employer"),
        ("candidate", "candidate"),
    )
    role = models.CharField(max_length=15, choices=options, default="candidate")

    @property
    def is_candidate(self):
        return self.role == "candidate"

    @property
    def is_employer(self):
        return self.role == "employer"


