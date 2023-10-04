from django.urls import path
from .views import QuizList,QuizDetail,QuestionList,QuestionDetail,OptionList,OptionDetail

urlpatterns = [
    path('quiz/', QuizList.as_view()),
    path('quiz/<int:pk>/', QuizDetail.as_view()),

    path('quiz/<int:quiz_id>/question/',QuestionList.as_view()),
    path('quiz/<int:quiz_id>/question/<int:pk>/',QuestionDetail.as_view()),

    path('quiz/<int:quiz_id>/question/<int:question_id>/option/',OptionList.as_view()),
    path('quiz/<int:quiz_id>/question/<int:question_id>/option/<int:pk>/',OptionDetail.as_view()),
    

]