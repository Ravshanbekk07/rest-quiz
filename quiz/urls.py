from django.urls import path
from .views import QuizList,QuizDetail

urlpatterns=[
    path('quiz/', QuizList.as_view()),
    path('quiz/<int:pk>/', QuizDetail.as_view())
]