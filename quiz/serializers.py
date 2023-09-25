from .models import Quiz,Question
from rest_framework import serializers
from django.contrib.auth.models import User
class QuizSerializer(serializers.ModelSerializer):
    class meta:
        model=Quiz
        fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class meta:
        model=Question
        fields="__all__"

class UserSerializer(serializers.Serializer):
    tasks = QuizSerializer(many=True,read_only=True)
    class  meta:
        model =User
        fields = ('id','username','tasks')
