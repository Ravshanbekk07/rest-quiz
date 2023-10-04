from django.urls import path
from .views import QuizList,QuizDetail,QuestionList,QuestionDetail

urlpatterns=[
    path('quiz/', QuizList.as_view()),
    path('quiz/<int:pk>/', QuizDetail.as_view()),

    path('quiz/<int:quiz_id>/question/',QuestionList.as_view()),
    path('quiz/<int:quiz_id>/question/<int:pk>/',QuestionDetail.as_view()),

]