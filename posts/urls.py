from django.urls import path, include
from posts.views import (
    detail_posts, 
    create_posts, 
    edit_posts, 
    delete_comments,
    edit_comments
)

urlpatterns = [
    path('<int:posts_id>/', detail_posts, name="detail-posts"),
    path('<int:posts_id>/edit/', edit_posts, name="edit-posts"),
    path('<int:posts_id>/quiz/', include(('quiz.urls','quiz'), namespace='quiz')),
    path('create/', create_posts, name="create-posts"),
    path('comments/<int:comments_id>/delete/', delete_comments, name="delete-comments"),
    path('comments/<int:comments_id>/edit/', edit_comments, name="edit-comments")
    
]           