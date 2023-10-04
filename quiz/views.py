from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Quiz,Question,Option,Take
from .serializers import QuizSerializer,QuestionSerializer,OptionSerializer,TakeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


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
            quiz = get_object_or_404(Quiz,id=pk)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        else:
            quiz.delete()
            return Response({"status":'deleted'})
       
    

class QuestionList(APIView):
    authentication_classes=[TokenAuthentication]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request,quiz_id):
        user=request.user
        if not user:
               
                return Response({'error': 'Unauthorized'}, status=401)
        if not quiz_id:
                    return Response({"error":'quiz id is required'})
           
        else:
                try:
                    quiz = Quiz.objects.get(id=quiz_id)
                except Quiz.DoesNotExist:
                    return Response({"error": "quiz not found."})
                questions = Question.objects.filter(quiz=quiz).all()
                serializer=QuestionSerializer(questions,many=True)
                return Response(serializer.data)

    def post(self,request,quiz_id):
            data=request.data

            user=request.user
                     
            if not quiz_id:
                    return Response({"error":'quiz id is required'})
            if not user:
                   
                    return Response({'error': 'Unauthorized'}, status=401)
            elif not user.is_superuser:
                return Response({'error': 'Forbidden'}, status=403)
            else:
                try:
                    quiz=Quiz.objects.get(id=quiz_id)
                except Quiz.DoesNotExist:
                    return Response({'error': 'quiz not found'}, status=401)
                data['quiz'] = quiz.pk
                serializer=QuestionSerializer(data=data)
                
                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
         
class QuestionDetail(APIView):
    authentication_classes=[TokenAuthentication]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,quiz_id,pk:int):

        user=request.user
        if not user:
             
                return Response({'error': 'Unauthorized'}, status=401)
        if not quiz_id:
                return Response({"error":'quiz id is required'})
           
        else:
                
                    quiz = get_object_or_404(Quiz,id=quiz_id)
                    question = get_object_or_404(Question,quiz=quiz,id=pk)
                    serializer=QuestionSerializer(question)
                    return Response(serializer.data)

    def put(self,request,quiz_id,pk:int):
        
        data=request.data
        user=request.user
       
        quiz=get_object_or_404(Quiz,id=quiz_id)    
        data['quiz']=quiz.pk
        question = get_object_or_404(Question,quiz=quiz,id=pk)
        
        serializer=QuestionSerializer(question,data=data)
        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    def delete(self,request,quiz_id,pk:int):
        user=request.user
      
        quiz = get_object_or_404(Quiz,id=pk)
        question = get_object_or_404(Question,quiz=quiz,id=pk)

        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        else:
            question.delete()
            return Response({"status":'deleted'})

class OptionList(APIView):
    authentication_classes=[TokenAuthentication]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated] 

    def get(self,request,quiz_id,question_id):
        user=request.user
        if not user:
               
                return Response({'error': 'Unauthorized'}, status=401)
        if not quiz_id:
                    return Response({"error":'quiz id is required'})
        if not question_id:
                    return Response({"error":'question id is required'})
              
        else:
               
                    quiz = get_object_or_404(Quiz,id=quiz_id)
                    question=get_object_or_404(Question,quiz=quiz,id=question_id)
                
                    options = Option.objects.filter(question=question).all()
                    serializer=OptionSerializer(options,many=True)
                    return Response(serializer.data)

    def post(self,request,quiz_id,question_id):
            data=request.data
            user=request.user
            if not quiz_id:
                    return Response({"error":'quiz id is required'})
            if not question_id:
                    return Response({"error":'question id is required'})
           
            if not user:
                   
                    return Response({'error': 'Unauthorized'}, status=401)
            elif not user.is_superuser:
                return Response({'error': 'Forbidden'}, status=403)
            else:
                quiz = get_object_or_404(Quiz,id=quiz_id)
                question=get_object_or_404(Question,quiz=quiz,id=question_id)
               
                data['question'] = question.pk
                serializer=OptionSerializer(data=data)
                
                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
            
    
class OptionDetail(APIView):
    authentication_classes=[TokenAuthentication]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]                        
    def get(self,request,quiz_id,question_id,pk:int):
           
        user=request.user
        if not user:
                    return Response({'error': 'Unauthorized'}, status=401)
        if not quiz_id:
                    return Response({"error":'quiz id is required'})
        if not question_id:
                    return Response({"error":'question id is required'})
                       
        else:
                    quiz = get_object_or_404(Quiz,id=quiz_id)
                    question=get_object_or_404(Question,quiz=quiz,id=question_id)
                    option=get_object_or_404(Option,question=question,id=pk)


                    serializer=OptionSerializer(option)
                    return Response(serializer.data)

    def put(self,request,quiz_id,question_id,pk):
            data=request.data
            user=request.user
            if not quiz_id:
                    return Response({"error":'quiz id is required'})
            if not question_id:
                    return Response({"error":'question id is required'})
           
            if not user:
                   
                    return Response({'error': 'Unauthorized'}, status=401)
            elif not user.is_superuser:
                return Response({'error': 'Forbidden'}, status=403)
            else:
                quiz = get_object_or_404(Quiz,id=quiz_id)
                question=get_object_or_404(Question,quiz=quiz,id=question_id)
                option=get_object_or_404(Option,question=question,id=pk)

                data['question'] = question.pk
                serializer=OptionSerializer(option,data=data)
                
                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)

    def delete(self,request,quiz_id,question_id,pk:int):
        user=request.user
      
        quiz = get_object_or_404(Quiz,id=quiz_id)
        question=get_object_or_404(Question,quiz=quiz,id=question_id)
        option=get_object_or_404(Option,question=question,id=pk)

        if not user:
                return Response({'error':'unauthorized'},status =401)
        elif not user.is_superuser:
                return Response({'error':'forbidden'},status=403)
           
        else:
            option.delete()
            return Response({"status":'deleted'})
        
class TakeList(APIView):
    authentication_classes=[TokenAuthentication]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,quiz_id):
        user=request.user
        if not user:
               
                return Response({'error': 'Unauthorized'}, status=401)
        if not quiz_id:
                    return Response({"error":'quiz id is required'})
        
        else:
               
                    quiz = get_object_or_404(Quiz,id=quiz_id)
                    takes=Take.objects.filter(quiz=quiz).all()
                    serializer=TakeSerializer(takes,many=True)
                    return Response(serializer.data)
    def post(self,request,quiz_id):
          
              

class TakeDetail(APIView):
    pass

