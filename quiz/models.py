from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quiz(models.Model):
    name=models.CharField(max_length=64)
    description=models.TextField(max_length=70)
    def __str__(self):
        return self.name

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    content=models.TextField()

    def __str__(self) -> str:
        return self.content[:50]