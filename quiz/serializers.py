from .models import Quiz,Question
from rest_framework import serializers
from django.contrib.auth.models import User
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"

    
class UserSerializer(serializers.Serializer):
    tasks = QuizSerializer(many=True,read_only=True)
    class  Meta:
        model = User
        fields = ('id','username','tasks')
