from django.urls import path
from quiz.views import (
    list_quiz, 
    get_quiz, 
    get_uuid_post,
    create_quiz,
    create_question,
    delete_question
)

urlpatterns = [
    path('', list_quiz, name="list-quiz"),
    path('get-uuid/', get_uuid_post, name="get-uuid"),
    path('api/<uuid:quiz_id>/', get_quiz, name="get-quiz"),
    path('create/', create_quiz, name="create-quiz"),
    path('create-question/<uuid:quiz_id>/', create_question, name="create-question"),
    path('delete-question/<uuid:question_id>/', delete_question, name="delete-question"),

]