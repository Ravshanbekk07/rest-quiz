from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Quiz,Question
from .serializers import QuizSerializer,QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token



class QuizList(APIView):
    authentication_classes=[TokenAuthentication]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        user=request.user
        #quiz=user.quiz
        quiz=Quiz.objects.all()
        serializer=QuizSerializer(quiz,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data =request.data
        user=request.user
        serializer = QuizSerializer(data=data)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class QuizDetail(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    authentication_classes=[BasicAuthentication]
    
    def get(self,request,pk:int):
        user=request.user
        try:
            if not user:
                return Response({'error':'unauthorized'},status =401)
            else:
                quiz=Quiz.objects.get(id=pk)
                serializer=QuizSerializer(quiz)
                return Response(serializer.data)
        except Quiz.DoesNotExist:
            return Response(
            data={'error':'task doesnt exist'},
            status=status.HTTP_404_NOT_FOUND)


    def put(self,request,pk:int):
        user=request.user
        try:
            quiz=Quiz.objects.get(id=pk)    
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=QuizSerializer(instance=quiz,data=request.data)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk:int):
        user=request.user
        try:
            quiz=Quiz.objects.get(id=pk)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=QuizSerializer(instance=quiz,data=request.data)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        elif serializer.is_valid():
            quiz.delete()
            return Response({"status":'deleted'})
        return Response(serializer.errors)
    

