from django.contrib import admin
from django.urls import path, include
from .views import quizlist, quiz_play,leaderboard
urlpatterns = [
    path("quizlist/", quizlist, name="quizlist"),
    path("<int:quiz_id>/play/", quiz_play, name="play_quiz"),
    path("<int:quiz_id>/leaderboard/", leaderboard, name="leaderboard"),
]
