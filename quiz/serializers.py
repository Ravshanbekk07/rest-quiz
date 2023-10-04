from .models import Quiz,Question,Option,Take
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

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Option
        fields="__all__"  

class TakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Take
        fields="__all__" 

class UserSerializer(serializers.Serializer):
    tasks = QuizSerializer(many=True,read_only=True)
    class  Meta:
        model = User
        fields = ('id','username','tasks')
