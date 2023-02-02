from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home" ),
    path('api/get-Quiz/', views.getQuiz, name="get_Quiz"),
    path('quiz/', views.quiz , name="quiz")
]
