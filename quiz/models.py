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
    
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.content[:50]
    
class Take(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.quiz.name

class Response(models.Model):
    take = models.ForeignKey(Take, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question.content[:50] + ' - ' + self.option.content[:50]
