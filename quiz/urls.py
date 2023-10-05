from django.urls import path
from .views import (QuizList,QuizDetail,
                    QuestionList,QuestionDetail,
                    OptionList,OptionDetail,
                    TakeList,TakeDetail,
                    ResponseList,ResponseDetail)

urlpatterns = [
    path('quiz/', QuizList.as_view()),
    path('quiz/<int:pk>/', QuizDetail.as_view()),

    path('quiz/<int:quiz_id>/question/',QuestionList.as_view()),
    path('quiz/<int:quiz_id>/question/<int:pk>/',QuestionDetail.as_view()),

    path('quiz/<int:quiz_id>/question/<int:question_id>/option/',OptionList.as_view()),
    path('quiz/<int:quiz_id>/question/<int:question_id>/option/<int:pk>/',OptionDetail.as_view()),
    
    path('quiz/<int:quiz_id>/take/',TakeList.as_view()),
    path('quiz/<int:quiz_id>/take/<int:pk>/',TakeDetail.as_view()),
    
    path('quiz/take/<int:take_id>/answer/',ResponseList.as_view()),
    path('quiz/take/<int:take_id>/result/',ResponseDetail.as_view()),

]