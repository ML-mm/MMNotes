from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: joined at {self.joined.strftime('%H:%M  %d/%m/%y')}"
