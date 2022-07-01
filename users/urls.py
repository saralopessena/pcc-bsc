from django.urls import path, include
from users.views import create_users, edit_users, login_users, logout_users, list_users_unique, edit_password

urlpatterns = [
    path('create/', create_users, name="create-users"),
    path('edit/', edit_users, name="edit-users"),
    path('login/', login_users, name="login-users"),
    path('logout/', logout_users, name="logout-users"),
    path('profile/', list_users_unique, name="profile-users"),
    path('edit-password/', edit_password, name="edit-password"),
]